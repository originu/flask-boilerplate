# Introduction
This boilerplate is for python server development which you want to develop web application based on AWS


# Setup
1. install python 3.8.x or higher version
2. install virtualenv
```
$ pip install virtualenv
```
** how to uninstall. if it doesn't work, you need to uninstall and install it
```
$ pip uninstall virtualenv
```    
3. clone git
```
$ git clone https://github.com/originu/flask-boilerplate.git
```
4. install modules of python
```
$ virtualenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```
** how to export module that you use to requirements.txt  
```
$ pip freeze > requirements.txt
```
5. install docker referring to https://docs.docker.com/engine/install/

6. install docker-compose referring to https://docs.docker.com/compose/install/    



# How to migrate and upgrade DB
- common 
    - app.py automatically finds modules of entity names *_entity.py and imports the modules so that flask migrate recognizes and generate a alembic file to a directory of migrations/versions
    - for example, add an entity python module like user_entity.py in a directory of app/entity 
- for linux user
```
$ export FLASK_APP="main.py"
$ flask db migrate -m 'migration message'          <= after this command, a migration file will be in migration/versions.
$ flask db upgrade                                 <= after this command, you will be able to see changes in DB
```

- for windows user
```
> $env:FLASK_APP="main.py"
> flask db migrate -m 'migration message'          <= after this command, a migration file will be in migration/versions.
> flask db upgrade                                 <= after this command, you will be able to see changes in DB
```


# How to run
```
$ docker-compose -f ./docker/backend.xml up -d
$ docker-compose -f ./docker/kafka-ui.xml up -d
$ docker ps --all
$ python main.py
open "http://localhost:8989" in a web browser so that you connect kafka-ui 
```
```
$ curl http://localhost:5000/api/server/version
```

# How to add new API 
1. go to a directory of resource/api
2. add new resource.py like server_resource.py. but the resource.py has to end to *_resource.py so that app.py imports all of *_resource.py files automatically.
3. you can add some API in new resource.py

# How to add new hook
1. go to a directory of resource/hook
2. add new hook.py like api_hook.py. but the hook.py has to end to *_hook.py so that app.py imports all of *_hook.py files automatically.
3. you can add some hooks in new hook.py

# How to setup for flask-migrate based on alembic
- for linux user
```
$ export FLASK_APP="main.py"
$ flask db init
```

- for windows user
```
> $env:FLASK_APP="main.py"
> flask db init
```





# Stack
docker   
docker-compose   
mysql   
mongodb  
redis  
kafka  
AWS Cloudwatch   
AWS S3   
gunicorn   
nginx   
flask   
flask-jwt-extended   
flask-migrate   
sqlalchemy


# Backlog
schedule   
pydantic   
OpenAPI   
flask-monitoring dashboard      
kafka-python   
python-eureka-client(as a MSA)       
scouter(as a APM)   
https://github.com/scouter-project/scouter/blob/master/README_kr.md   
https://pypi.org/project/scout-apm/   

