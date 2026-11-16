# Hexa Rdzen - straznik: jesli rdzen nie odpowiada, uruchom go ponownie (co 5 min z Harmonogramu).
$ok = $false
try { $r = Invoke-RestMethod 'http://100.67.199.43:8770/zdrowie' -TimeoutSec 4; $ok = [bool]$r.ok } catch {}
if (-not $ok) {
  Start-Process -FilePath (Get-Command python).Source -ArgumentList 'C:\Hexa\rdzen\rdzen.py' -WorkingDirectory 'C:\Hexa\rdzen' -WindowStyle Hidden
  Add-Content C:\Hexa\rdzen\rdzen.log ((Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + ' straznik: uruchomiono rdzen')
}
