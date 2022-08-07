conda activate py38
write-host "run flask"
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

flask run
