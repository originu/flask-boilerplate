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
- for linux user
```
$ export FLASK_APP="main.py"

$ flask db migrate
$ flask db upgrade
```

- for windows user
```
> $env:FLASK_APP="main.py"
> flask db migrate
> flask db upgrade
```


# How to run
```
$ docker-compose -f ./docker/backend.xml up -d
$ docker ps --all
$ python main.py
```
```
$ curl http://localhost:5000/api/server/version
```
#  

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

