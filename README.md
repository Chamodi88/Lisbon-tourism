# Lisbon-tourism
Group project seminar, Master of Geospatial Technologies, NOVA IMS

This application has been developed using Geodjango to provide information on tourists attractions in Lisbon and determined the nearest locations based on the user's current location.

Requirements - python - postgreSQL - django - Libraries (GEOS, GDAL, PROJ.4, PostGIS) - django-leaflet - crspy-forms

Installation

1. Create a database for the project
2. Change database settings inside the settings.py to match with yours
3. Run following commands in the commad prompt pointing to the project folder
        - python manage.py makemigrations
        - python manage.py migrate
4. upload the data using following command in the commad prompt pointing to the data folder ogr2ogr.exe -f "PostgreSQL" PG:"dbname=dbname user=username password=password" "data.shp" -nln "appgps_attraction" -append
5. Go back to the folder where manage.py is and run the following command to turn on the server python manage.py runserver
6. Open the web browser and navigate to http://localhost:8000/appgps/
