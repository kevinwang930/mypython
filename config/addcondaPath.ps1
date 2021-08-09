$addPath = "D:\miniconda3;D:\miniconda3\Scripts"
$arrPath = [Environment]::GetEnvironmentVariable('Path', 'User') -split ';' | Where-Object { $_ -notlike "*miniconda*" } 

$arrPath = $arrPath | Where-Object { -not [string]::IsNullOrEmpty($_) }


$newPath = ($arrPath + $addPath) -join ';'
Write-Output $newPath
# $env:Path = $arrPath
# $env:Path = $arrPath -join ';'
[Environment]::SetEnvironmentVariable("Path", $newPath, 'User')