# Fetch the audio track (16 kHz mono WAV) for one lecture from a signed
# Kaltura HLS manifest URL.
#
#   .\fetch_audio.ps1 -UrlFile manifest.txt -Out FTC03.wav -OutDir C:\path\to\audio
#
param(
  [Parameter(Mandatory=$true)][string]$UrlFile,
  [Parameter(Mandatory=$true)][string]$Out,
  [string]$OutDir = "C:\Users\thana\AppData\Local\Temp\opencode\ftc_audio"
)
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$url = (Get-Content $UrlFile -Raw).Trim()
$target = Join-Path $OutDir $Out
ffmpeg -y -hide_banner -loglevel warning -i $url -vn -ac 1 -ar 16000 -c:a pcm_s16le $target
Get-Item $target | Select-Object Name, @{N='MB';E={[math]::Round($_.Length/1MB,1)}}
