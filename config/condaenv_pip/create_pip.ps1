conda create -n pipenv python=3.8 -c conda-forge
conda activate pipenv
if ($?) {
    $filePath = Join-Path -Path $PSScriptRoot -ChildPath "envpip_packages.txt"
    pip install -r $filePath

    }

