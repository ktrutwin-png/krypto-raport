# HEXA RDZEŃ – instalacja na serwerze (C:\Hexa\rdzen). Uruchamia Mózg: powershell -File instaluj.ps1
$ErrorActionPreference = 'Stop'
$log = 'C:\Hexa\rdzen_instaluj.log'
"start $(Get-Date)" | Out-File $log -Encoding utf8
git -C C:\Hexa\krypto-raport pull -q --rebase 2>&1 | Out-File $log -Append -Encoding utf8
New-Item -ItemType Directory -Force C:\Hexa\rdzen\rozmowy | Out-Null
Copy-Item C:\Hexa\krypto-raport\tools\rdzen\rdzen.py, C:\Hexa\krypto-raport\tools\rdzen\hexa.md C:\Hexa\rdzen\ -Force
if (-not (Test-Path C:\Hexa\rdzen\pamiec_hexy.md)) { "# Pamięć Hexy – fakty, które szef kazał zapamiętać" | Out-File C:\Hexa\rdzen\pamiec_hexy.md -Encoding utf8 }
if (-not (Test-Path C:\Hexa\rdzen\token.txt)) {
  $b = New-Object byte[] 24; [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($b)
  ([Convert]::ToBase64String($b) -replace '[+/=]','x') | Out-File C:\Hexa\rdzen\token.txt -Encoding ascii -NoNewline
}
$ts = (& 'C:\Program Files\Tailscale\tailscale.exe' ip -4 2>$null | Select-Object -First 1)
"tailscale=$ts" | Out-File $log -Append -Encoding utf8
# zapora: port 8770 tylko z sieci Tailscale
if (-not (Get-NetFirewallRule -DisplayName 'Hexa Rdzen 8770 (tylko Tailscale)' -EA SilentlyContinue)) {
  New-NetFirewallRule -DisplayName 'Hexa Rdzen 8770 (tylko Tailscale)' -Direction Inbound -Protocol TCP -LocalPort 8770 -RemoteAddress 100.64.0.0/10 -Action Allow | Out-Null
}
# zadanie: start przy uruchomieniu serwera + restart co 5 min, jeśli padnie
$py = (Get-Command python).Source
$act = New-ScheduledTaskAction -Execute $py -Argument 'C:\Hexa\rdzen\rdzen.py' -WorkingDirectory 'C:\Hexa\rdzen'
$trg = New-ScheduledTaskTrigger -AtStartup
$set = New-ScheduledTaskSettingsSet -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 5) -ExecutionTimeLimit ([TimeSpan]::Zero) -StartWhenAvailable
Register-ScheduledTask -TaskName 'Hexa Rdzen' -Action $act -Trigger $trg -Settings $set -User 'SYSTEM' -RunLevel Highest -Force | Out-Null
Stop-ScheduledTask -TaskName 'Hexa Rdzen' -EA SilentlyContinue
Start-ScheduledTask -TaskName 'Hexa Rdzen'
Start-Sleep 4
try { $z = Invoke-RestMethod "http://${ts}:8770/zdrowie" -TimeoutSec 5; "zdrowie=$($z.ok)" | Out-File $log -Append -Encoding utf8 } catch { "zdrowie BLAD $_" | Out-File $log -Append -Encoding utf8 }
"koniec $(Get-Date)" | Out-File $log -Append -Encoding utf8
