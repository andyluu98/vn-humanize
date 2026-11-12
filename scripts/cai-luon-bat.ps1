# Cai (hoac go) khoi "luon bat" cua vn-humanize vao CLAUDE.md cua nguoi dung.
# Chay lai nhieu lan khong chen trung: khoi cu duoc thay bang khoi moi.
# Truoc moi lan ghi, ban cu cua CLAUDE.md duoc chep vao _backup\ canh file.
# Thong bao viet khong dau de chay dung tren Windows PowerShell 5.1.
param(
    [switch]$Go,
    [string]$ClaudeMd = (Join-Path $HOME ".claude\CLAUDE.md")
)
$ErrorActionPreference = "Stop"

$BatDau = "<!-- vn-humanize:bat-dau -->"
$KetThuc = "<!-- vn-humanize:ket-thuc -->"
$Utf8 = New-Object System.Text.UTF8Encoding($false)
$Nguon = Join-Path (Split-Path $PSScriptRoot -Parent) "luon-bat.md"
$Mau = "(?s)\r?\n?" + [regex]::Escape($BatDau) + ".*?" + [regex]::Escape($KetThuc) + "\r?\n?"

function Sao-Luu([string]$Duong) {
    $Thu = Join-Path (Split-Path $Duong -Parent) "_backup"
    New-Item -ItemType Directory -Force -Path $Thu | Out-Null
    $Ten = [IO.Path]::GetFileNameWithoutExtension($Duong) + "_" + (Get-Date -Format "yyMMdd-HHmm") + [IO.Path]::GetExtension($Duong)
    $Dich = Join-Path $Thu $Ten
    $k = 2
    while (Test-Path -LiteralPath $Dich) {
        $Dich = Join-Path $Thu ([IO.Path]::GetFileNameWithoutExtension($Ten) + "-$k" + [IO.Path]::GetExtension($Ten)); $k++
    }
    Copy-Item -LiteralPath $Duong -Destination $Dich -Force
    Write-Host "Da sao luu ban cu: $Dich"
}

$CoFile = Test-Path -LiteralPath $ClaudeMd
$Cu = if ($CoFile) { [IO.File]::ReadAllText($ClaudeMd, $Utf8) } else { "" }
$CoKhoi = $Cu.Contains($BatDau)

if ($Go) {
    if (-not $CoKhoi) { Write-Host "Khong thay khoi vn-humanize trong $ClaudeMd. Khong doi gi."; exit 0 }
    Sao-Luu $ClaudeMd
    $Xd = if ($Cu.Contains("`r`n")) { "`r`n" } else { "`n" }
    $Moi = [regex]::Replace($Cu, $Mau, $Xd)
    [IO.File]::WriteAllText($ClaudeMd, $Moi.TrimEnd() + $Xd, $Utf8)
    Write-Host "Da go khoi vn-humanize khoi $ClaudeMd"
    exit 0
}

if (-not (Test-Path -LiteralPath $Nguon)) { throw "Khong tim thay $Nguon" }
$TextNguon = [IO.File]::ReadAllText($Nguon, $Utf8)
$i = $TextNguon.IndexOf($BatDau)
$j = $TextNguon.IndexOf($KetThuc)
if ($i -lt 0 -or $j -lt $i) { throw "luon-bat.md thieu dong danh dau $BatDau hoac $KetThuc" }
$Khoi = $TextNguon.Substring($i, $j + $KetThuc.Length - $i).Replace("`r`n", "`n")

if ($CoFile) { Sao-Luu $ClaudeMd } else { New-Item -ItemType Directory -Force -Path (Split-Path $ClaudeMd -Parent) | Out-Null }

$Xd = if ($Cu.Contains("`r`n")) { "`r`n" } else { "`n" }
$Khoi = $Khoi.Replace("`n", $Xd)
$Goc = if ($CoKhoi) { [regex]::Replace($Cu, $Mau, $Xd) } else { $Cu }
$Goc = $Goc.TrimEnd()
$Moi = if ($Goc.Length -gt 0) { $Goc + $Xd + $Xd + $Khoi + $Xd } else { $Khoi + $Xd }
if ($CoKhoi) { Write-Host "Da cap nhat khoi vn-humanize trong $ClaudeMd" }
elseif ($Goc.Length -gt 0) { Write-Host "Da them khoi vn-humanize vao cuoi $ClaudeMd" }
else { Write-Host "Da tao $ClaudeMd voi khoi vn-humanize" }
[IO.File]::WriteAllText($ClaudeMd, $Moi, $Utf8)
Write-Host "Mo phien Claude Code moi de khoi co hieu luc. Go: chay lai script voi -Go"
