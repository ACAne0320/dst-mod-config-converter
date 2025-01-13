from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import re
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 获取当前文件所在目录
current_dir = Path(__file__).parent

# Mount static files with absolute path
app.mount("/static", StaticFiles(directory=str(current_dir / "static")), name="static")


def extract_workshop_ids(lua_content: str):
    """Extract enabled workshop IDs from modoverrides.lua content."""
    # 简化正则表达式，只匹配 workshop-数字
    pattern = r'workshop-(\d+)'
    matches = re.findall(pattern, lua_content)
    print(f"Found workshop IDs: {matches}")  # 调试信息
    return matches

def generate_dedicated_server_mods_setup(workshop_ids):
    """Generate the content for dedicated_server_mods_setup.lua."""
    lines = [f"ServerModSetup(\"{workshop_id}\")" for workshop_id in workshop_ids]
    return "\n".join(lines)

@app.post("/generate_mods_setup")
def generate_mods_setup(master: str = Form(...), caves: str = Form(...)):
    try:
        # Validate input
        if len(master) > 1000000 or len(caves) > 1000000:  # 限制输入大小
            raise HTTPException(status_code=400, detail="Input file too large")
        
        print(f"Received master content: {master[:100]}...")  # 调试信息
        print(f"Received caves content: {caves[:100]}...")    # 调试信息
        
        # Extract workshop IDs from both files
        master_ids = extract_workshop_ids(master)
        caves_ids = extract_workshop_ids(caves)

        print(f"Master IDs: {master_ids}")  # 调试信息
        print(f"Caves IDs: {caves_ids}")    # 调试信息

        # Combine and deduplicate workshop IDs
        all_ids = sorted(set(master_ids + caves_ids))
        
        if not all_ids:
            return JSONResponse(content={
                "content": "",
                "warning": "No enabled mods found in the provided files"
            })
            
        # Generate the content
        setup_content = generate_dedicated_server_mods_setup(all_ids)
        print(f"Generated content: {setup_content}")  # 调试信息
        
        # Return the content directly as JSON
        return JSONResponse(content={"content": setup_content})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def index():
    return {"message": "Upload your modoverrides.lua content to generate the setup file."}
