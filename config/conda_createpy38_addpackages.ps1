conda create -n py38 python=3.8 -c conda-forge
if ($?) {
    $filePath = Join-Path -Path $PSScriptRoot -ChildPath "conda_py38_packages.txt"
    conda install -n py38 --file $filePath -c conda-forge

    }

