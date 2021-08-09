$parentPath = Split-Path  $PSScriptRoot -Parent

$pythonPath = Join-Path -Path $parentPath -ChildPath "project\module"
$pythonPath
[Environment]::SetEnvironmentVariable("PYTHONPATH", $pythonpath, 'User')