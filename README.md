# **WAKEM-API**

## Getting started
- Upgrade Pip
> `pip install --upgrade pip`
- Install Virtualenv
> `python -m venv venv`
- Activating Virtualenv
> `.\venv\Scripts\activate.ps1`

## Creating tables
Switch to flask shell
```
flask --app "src/app:create_app('local')" shell
from src.app import db
db.create_all()
```

## Launch application (Developper only)
```
set FLASK_DEBUG=True ou $ENV:FLASK_DEBUG=1
set FLASK_APP=src/app.py ou $ENV:FLASK_APP=src\app.py
flask --app "src/app:create_app('local')" run
```


## Getting Ready
- PG Admin, latest version or PostgreSQL Client (Dbeaver)
- Pycharm or VS code for Api
- Ionic 6 for mobile part


## Notes and references
- docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
- docker run --name fs_instance -e POSTGRES_PASSWORD=password -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -d postgres:latest
- docker exec -it fs_instance psql -U postgres
- CREATE USER technical_user WITH SUPERUSER PASSWORD 'faVNeqG4S?'; \\ Example password and user
- CREATE DATABASE wakem
- docker run --name fs_instance -e POSTGRES_PASSWORD=faVNeqG4S?.w2$u -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -d postgres:latest  \\ Example password and user
- docker run 
- 
- python -m pip install PACKAGENAME --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
- [Lien vers le tutoriel jwt auth](https://www.bacancytechnology.com/blog/flask-jwt-authentication)