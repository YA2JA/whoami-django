# whoami-django
**[Run it on local machine](#run-on-local-machine)**<br>
**[Run it on heroku](#run-on-heroku)**<br>

## Download and open  project:
  Download:
  ```
  git clone https://github.com/YA2JA/whoami-django.git
  ```
  to open directory:
  ```
  cd whoami-django
  ```
***
<br>
## Install and run virtualenv. not mandatory
### Linux
Install:
```
sudo pip install virtualenv
```
Run:
```
virtualenv env_dir_name
source env_dir_name/bin/activate
```
***

### Mac
Install:
```
pip install virtualenv
```
Run:
```
virtualenv env_dir_name
source env_dir_name/bin/activate
```
***
### Windows
Install:
```
pip install virtualenv
```
Run:
```
python -m venv env_dir_name
env_dir_name\Scripts\activate.bat
```
***

## Run on local machine
  **I recomend to do that in virtual envirenement, [here instructions](#install-and-run-virtualenv)**<br>, [for more info](https://pythontips.com/2013/07/30/what-is-virtualenv/)
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

