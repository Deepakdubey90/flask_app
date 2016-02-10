Flask App
==

##Setup

### Requirements
* Python 2.7.6

### Installation
* Clone the repository  ```$ git clone https://github.com/Deepakdubey90/flask_app.git```
* CD into the repository dir ```$ cd flask_app/```
* Create a virtualenv ```$ virtualenv venv```
* Activate it ```$ source venv/bin/activate```
* Install the required libraries ```$ pip install -r requirements.txt```
* create local settings by ```$ cp src/settings/local_settings.py src/settings/local.py```

### Database setup
* Initialize database  ```$ python src/manage.py db init```
* Create migration by running ```$ python src/manage.py db migrate```
* Upgrade database by by running ```$ python src/manage.py db upgrade```

### Running the app
* ```$ python src/manage.py runserver```

### Test data on rest-api
* show list of all users ```http://127.0.0.1:5000/api/user```
* show specific user details ```http://127.0.0.1:5000/api/user/id```
