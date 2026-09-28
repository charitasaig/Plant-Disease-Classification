# PowerShell launcher for PlantGuard AI Streamlit Application
Write-Host "========================================================" -ForegroundColor Green
Write-Host "  Starting Plant Disease Classifier (Streamlit App)    " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green

Set-Location -Path $PSScriptRoot

try {
    python -m streamlit --version | Out-Null
} catch {
    Write-Host "Installing requirements..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host "`nLaunching Streamlit web application in your browser..." -ForegroundColor Cyan
python -m streamlit run app.py
