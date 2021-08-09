$conda = conda env list --json | ConvertFrom-Json
$result = $false
foreach ($env in $conda.envs) {
    if ($env.ToLower().Contains('py38')) {
        $result = $true
    }
}
if ($result) {
    $filePath = Join-Path -Path $PSScriptRoot -ChildPath "conda_py38_packages.txt"
    conda install -n py38 --file $filePath -c conda-forge
}
else {
    conda create -n py38 python=3.8 -c conda-forge
    if ($?) {
        $filePath = Join-Path -Path $PSScriptRoot -ChildPath "conda_py38_packages.txt"
        conda install -n py38 --file $filePath -c conda-forge

    }
}