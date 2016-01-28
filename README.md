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

### Database setup
* Initialize database  ```$ python manage.py db init```
* Create migration by running ```$ python manage.py db migrate```
* Upgrade database by by running ```$ python manage.py db upgrade```

### Running the app
* ```$ python manage.py runserver```

### Test data on rest-api
* show list of all users ```http://127.0.0.1:5000/api/user```
* show specific user details ```http://127.0.0.1:5000/api/user/id```
