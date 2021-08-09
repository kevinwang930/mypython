$fileDir = Join-Path -Path $env:USERPROFILE -ChildPath "pip"

If (!(test-path $fileDir)) {
    New-Item -ItemType Directory -Force -Path $fileDir
}

$filePath = Join-Path -Path $PSScriptRoot -ChildPath "pip.ini"
Copy-Item -Path $filePath -Destination $fileDir
