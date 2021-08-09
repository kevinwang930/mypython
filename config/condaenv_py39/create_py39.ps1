conda create -n py39 python=3.9 -c conda-forge
if ($?) {
    $filePath = Join-Path -Path $PSScriptRoot -ChildPath "requirements.txt"
    conda install -n py39 --file $filePath -c conda-forge
    }

