async function generateSetup() {
    const masterContent = document.getElementById('master').value;
    const cavesContent = document.getElementById('caves').value;

    // 添加调试信息
    console.log('Master content length:', masterContent.length);
    console.log('Caves content length:', cavesContent.length);

    if (!masterContent && !cavesContent) {
        alert('Please paste at least one modoverrides.lua content');
        return;
    }

    const formData = new FormData();
    formData.append('master', masterContent);
    formData.append('caves', cavesContent);

    try {
        const response = await fetch('/generate_mods_setup', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Received response:', data); // 调试信息
            if (!data.content) {
                console.error('Empty content received');
                alert('No mod IDs found in the provided files. Please check your input.');
                return;
            }
            document.getElementById('result').value = data.content;
        } else {
            const errorText = await response.text();
            console.error('Server error:', errorText);
            alert('Error generating setup file: ' + errorText);
        }
    } catch (error) {
        console.error('Request error:', error);
        alert('Error generating setup file: ' + error.message);
    }
}

function copyToClipboard() {
    const resultText = document.getElementById('result');
    if (!resultText.value) {
        alert('No content to copy');
        return;
    }
    
    resultText.select();
    document.execCommand('copy');
    
    const copyButton = document.getElementById('copyButton');
    const originalText = copyButton.textContent;
    copyButton.textContent = 'Copied!';
    setTimeout(() => {
        copyButton.textContent = originalText;
    }, 2000);
}
