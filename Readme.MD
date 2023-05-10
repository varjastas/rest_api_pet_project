App written on Django REST API Framework. It has 2 endpoints: GET and IMPORT. You can import any data mentioned in test_data.json.
It can update data too if you send request to IMPORT endpoint with id of object you want to update.

Endpoints:
[POST] /import - endpoint which imports and parses data to database 
[GET] /detail/<nazev modelu>/ - list which contains all models based on their name 
[GET] /detail/<nazev modelu>/<id> - all data to specific id.

How to run: 
1. create venv: python -m venv venv
2. activate it: 
#windows machine
venv\Scripts\activate.bat
or venv\Scripts\activate if .bat isn`t working. You may need to set execution policies using this command:
Type Set-ExecutionPolicy Unrestricted to set the policy to Unrestricted
#mac/linux
source venv/bin/activate

(venv) should be shown in cmd if you`re using terminal of an IDE
3. installing requirements.txt: pip install -r backend/requirements.txt

4. Setting Secret_key to .env if you want

5. Making migrations:
cd backend 
python manage.py makemigrations
python manage.py migrate 

6. Setting the docker up: docker-compose up -d --build

7. Now you can run the client.py or make your own requests to server(default path = http://localhost:8000) or you can access the server in docker if you go to app terminal
