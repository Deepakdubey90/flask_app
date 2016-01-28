Flask App
==

##Setup

### Requirements
* Python 2.7.6
* sqlite


### Installation
* Clone the repository  ```$ git clone https://github.com/Deepakdubey90/flask_app.git```
* CD into the repository dir ```$ cd flask_app/```
* Create a virtualenv ```$ virtualenv venv```
* Activate it ```$ source venv/bin/activate```
* Install the required libraries ```$ pip install -r requirements.txt```

### Database setup
* Initialize database  ```$ python manage.py init db```
*Create migration by running '''$ python manage.py db migrate'''
*Upgrade database by by running '''$ python manage.py db upgrade'''

### Running the app
* ```$ python manage.py runserver```
