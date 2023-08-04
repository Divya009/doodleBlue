# doodleBlue
For the Assignment Test, using Python  + Django framework

cloning the project -
```git clone <url>```

go to the project director, i.e. doodleBlue, and create virtualenv - python 3.10
```virtualenv venv```

run this command to add project dependencies - 
``` pip install -r requirements.txt```

run this command to add system dependencies for redis server - 
	1. macOS -
  		```brew install redis```
  		```brew services restart redis```
  		in the use tab run this command - ```redis-server```
	2. Ubuntu - 
  		```sudo apt install redis-server```
  		```sudo service redis-server start```
	3. windows - 
  		``` Refer this link - (https://redis.io/download)```

run this command - 
```python manage.py migrate```

run this command - 
```python manage.py runserver```
