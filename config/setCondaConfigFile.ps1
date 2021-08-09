$filePath = Join-Path -Path $PSScriptRoot -ChildPath ".condarc"

Copy-Item -Path $filePath -Destination $env:USERPROFILE