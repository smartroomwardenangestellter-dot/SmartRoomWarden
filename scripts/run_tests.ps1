param(
  [string]$Python = ".venv\Scripts\python.exe"
)
Write-Host "Running tests with: $Python"
if (Test-Path $Python) {
    & $Python -m unittest discover -s tests -p 'test_*.py' -v
} else {
    python -m unittest discover -s tests -p 'test_*.py' -v
}

Write-Host "Tests completed."
