# whoami-django
**[Run it on local machine](#run-on-local-machine)**<br>
**[Run it on heroku](#run-on-heroku)**<br>

## Download the project:
  ```
  git clone https://github.com/YA2JA/whoami-django.git
  ```
***
<br>

## Run on local machine
  **I recomend to do that in virtual envirenement [here you can lern more](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)**<br>
  Download the project on your machine and open terminal in the project directory
  Install project dependency:
  ```
  pip insall -r requirements.txt
  ```
  Now you can run it! by writing
  ```
  manage.py runserver
  ```
  
***
<br>

## Run on heroku
  Download the project on your machine <br>
  
  Prepare heroku server:
  ```
  heroku login
  heroku git:remote -a your-project-name
  heroku config:set DEBUG_COLLECTSTATIC=1
  ```
  Now you can upload the project on server:
  ```
  git push heroku master
  ```
