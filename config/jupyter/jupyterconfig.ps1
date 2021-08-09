$fileDir = Join-Path -Path $env:USERPROFILE -ChildPath ".jupyter\nbconfig"

If (!(test-path $fileDir)) {
    New-Item -ItemType Directory -Force -Path $fileDir
}

$filePath = Join-Path -Path $PSScriptRoot -ChildPath "notebook.json"
Copy-Item -Path $filePath -Destination $fileDir