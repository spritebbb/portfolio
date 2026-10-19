# Regenerate the CJK display-font subset after any copy change.
#
# The headings use Noto Serif SC, but only the 617 (and counting) hanzi that
# actually appear in the source are downloaded, so the file stays ~113 KB
# instead of ~7 MB. Add new copy, run this, rebuild.
#
#   pwsh -File scripts/subset-cjk.ps1
#   npm run build

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$py = "C:\Users\sprite\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
$tmp = Join-Path $env:TEMP 'portfolio-han.txt'

& $py -c @"
import pathlib
root = pathlib.Path('.')
chunks = []
for pat in ('src/**/*.vue', 'src/**/*.ts', '*.html'):
    for p in root.glob(pat):
        chunks.append(p.read_text(encoding='utf-8', errors='ignore'))
han = sorted(set(ch for ch in '\n'.join(chunks) if '\u4e00' <= ch <= '\u9fff'))
pathlib.Path(r'$tmp').write_text(''.join(han), encoding='utf-8')
print('hanzi:', len(han))
"@

$chars = [System.IO.File]::ReadAllText($tmp, [System.Text.Encoding]::UTF8)
$enc = [System.Uri]::EscapeDataString($chars)
Write-Host "hanzi: $($chars.Length), encoded url: $($enc.Length) chars"

$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
$url = "https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700&text=$enc&display=swap"
$css = (Invoke-WebRequest -Uri $url -Headers @{ 'User-Agent' = $ua } -TimeoutSec 90).Content

$m = [regex]::Match($css, 'url\((https://[^)]+)\)')
if (-not $m.Success) { throw "Google Fonts returned no font URL. CSS head: $($css.Substring(0, [Math]::Min(200, $css.Length)))" }

$out = "src\assets\fonts\noto-serif-sc-700-cjk.woff2"
Invoke-WebRequest -Uri $m.Groups[1].Value -Headers @{ 'User-Agent' = $ua } -OutFile $out -TimeoutSec 120
$f = Get-Item $out
Write-Host "rebuilt $out : $([math]::Round($f.Length / 1kb, 1)) KB"
Write-Host "next: npm run build"
