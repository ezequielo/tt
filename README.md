# tt

## endpoints

Endpoint						              Metodos
/communities 					            [POST]
/communities/{name} 			        [GET, PUT, DELETE]
/communities/{name}/enrollments 	[POST]


## run locally

Ideally use virtual env

install packages
`pip install -r tt/requirements.txt`

export flask app
`export FLASK_APP app/app.py`

run app
`flask run`

Alternatively use `run.py` script
