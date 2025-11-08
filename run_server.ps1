# Runs the local server for the web app and opens the host link
# Usage: Right‑click > Run with PowerShell, or `powershell -ExecutionPolicy Bypass -File .\run_server.ps1`

param(
  [int]$Port = 8000
)

$Root = Join-Path $PSScriptRoot "web"

# Try to detect a usable IPv4 address for LAN access
try {
  $ip = (Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -notlike "169.*" -and $_.PrefixLength -lt 32 } |
    Select-Object -First 1 -ExpandProperty IPAddress)
} catch {
  $ip = $null
}
if (-not $ip) { $ip = "127.0.0.1" }

# Check if the port is already in use (another server running)
$portBusy = $false
try {
  $portBusy = Test-NetConnection -ComputerName localhost -Port $Port -InformationLevel Quiet
} catch {
  $portBusy = $false
}

Write-Host "Serving '$Root' on:" -ForegroundColor Cyan
Write-Host " - http://localhost:$Port/"
Write-Host " - http://$ip:$Port/"

if ($portBusy) {
  Write-Warning "Port $Port is already in use. Not starting a new server."
} else {
  # Start Python HTTP server in a new window
  Start-Process -WorkingDirectory $Root -FilePath "python" -ArgumentList "-m http.server $Port" -WindowStyle Normal
  Start-Sleep -Seconds 1
}

# Open the main page in the default browser
Start-Process "http://localhost:$Port/index.html"