# Python + django + gunicorn + nginx 

### Setup virtual environment. This separates the pip packges, project to project

Create a virtual environment called **dev-env** and activate the environment and check its correct  
```commandline
python3 -m venv dev-env 
source dev-env/bin/activate
echo $VIRTUAL_ENV
```

### Install the pip packages 
```commandline
pip install -r requirements.txt
```

### Running the service locally in Django
```commandline
nohup python manage.py runserver 
jobs -l or pgrep runserver
sudo lsof -n -P -i TCP:8000 -s TCP:LISTEN
kill 43689
```

### Running from gunicorn
```commandline
gunicorn -c config/gunicorn/dev.py  
tail -f /var/log/gunicorn/dev.log  
kill xxxxx
```

### Connect to Mongo 
```commandline
docker compose up
``` 
