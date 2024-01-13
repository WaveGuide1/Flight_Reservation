# Flight_Reservation
Flight Reservation REST API

# WHAT YOU NEED TO RUN THE APP LOCALLY

## (1) Clone the Project From GitHub
.. Run the following command to clone the project into the folder
.... git clone <repository-url>

## (2) Installation
.. pip install django
.. pip install mysqlclient
.. pip install djangorestframework
.. pip install python-dotenv (search how to connect it)

## (3) Create a Database (MySQL database was used in this project). You can Postgresql or any other sql db
### If you don't have mysql installed

.. Search on internet how to install mysql in your operating system.

### If mysql is installed in your OS and you are using linux, Follow the command below to create db.

.. Creating MySQL User and Database

.... mysql -u root -p

.. Now you can create a MySQL user which in our case we will call ‘name’,  ‘Password‘:

.... mysql> CREATE USER 'name'@'localhost' IDENTIFIED BY 'password';

.. Run the following command to create a database ‘flightDB‘:

.. To grant all permissions on the new database ‘flightDB‘ to the user ‘name‘ use the following command:

.... mysql> GRANT ALL PRIVILEGES ON flightDB.* TO 'name'@'localhost';

.. When you finish with setting up your MySQL permissions, make sure to reload all the privileges with:

.... mysql> FLUSH PRIVILEGES;

.. In settings.py, you need to connect the database to the application. Do this by replacing the database user, name, and password with your own local values:

.... DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'flightDB',
        'USER':'root',
        'PASSWORD':'password',
    }
}


## (4) Migrate Project to the Database

.. python3 manage.py makemigrations

.. python3 manage.py migrate


## (5) Run the Project

.. python manage.py runserver

.. If there are no errors, open http://127.0.0.1:8000/ in a web browser.


# Available Local Routes


## Authentication Routes

[POST] http://127.0.0.1:8000/api/token

ADD USER FROM ADMIN PANEL


## Flight Routes (Required Auth)


[DELETE] http://127.0.0.1:8000/api/flight_reservation/flight/<ID>/

[GET] http://127.0.0.1:8000/api/flight_reservation/flight/<ID>/

[GET] http://127.0.0.1:8000/api/flight_reservation/flight/

[POST] http://127.0.0.1:8000/api/flight_reservation/flight/

[PUT] http://127.0.0.1:8000/api/flight_reservation/flight/<ID>/


## Passenger Routes

[GET] http://127.0.0.1:8000/api/flight_reservation/passenger/<ID>/

[GET] http://127.0.0.1:8000/api/flight_reservation/passenger/

[PUT] http://127.0.0.1:8000/api/flight_reservation/passenger/<ID>/

[POST] http://127.0.0.1:8000/api/flight_reservation/passenger/

[DELETE] http://127.0.0.1:8000/api/flight_reservation/passenger/<ID>/


## Reservation Routes

[GET] http://127.0.0.1:8000/api/flight_reservation/reservation/

[GET] http://127.0.0.1:8000/api/flight_reservation/reservation/<ID>/

[DELETE] http://127.0.0.1:8000/api/flight_reservation/reservation/<ID>/

[PUT] http://127.0.0.1:8000/api/flight_reservation/reservation/<ID>


## Query Routes

Find Reservation
[POST] http://127.0.0.1:8000/api/flight_reservation/find_flight/
Required fields
operation_date
departure_country
arrival_country


Save Reservation
[POST] http://127.0.0.1:8000/api/flight_reservation/save_reservation/
Required fields
id (Flight_id)
first_name
last_name
email
mobile_number

