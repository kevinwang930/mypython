conda activate base
if ($?) {
    $test = "this is a test"
    conda list
    $test
    }