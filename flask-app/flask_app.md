# how to create Flask API in python
## 1. creating a virtual env for your python project
- conda manage virtual env\
    `$conda env list`(check the current env list)\
    `$conda create -n py38 python==3.8`(create your virtual env named py38)\
- activate your env\
    in your interpreter(if you are using pycharm, in settings->project->project interpreter-> add->conda environment)\
    or in command line click `$activate py38`(activate your env)\
- install some packages\
    `$ pip install -i http:---(domestic image)`\
    `$ pip list or pip freeze`(check whether you have installed the packages)\
  
- after install all the packages\
    `$ pip freeze > requirements.txt`(auto-create requirements.txt，save this requirement and its dependencies so App Platform can install them later)
        
## 2. creating mini flask app
here is an instance in [app.py](./app.py)


## 3. setting up your gunicorn configuration
- what is gunicorn ?\
    Gunicorn is a Python WSGI(web server gateway interface) HTTP server that many developers use to deploy their Python applications\-
  
### steps
  - `$ touch gunicorn_config.py` Open a file named `gunicorn_config.py`
  - Pushing the Site to GitHub\
    link to  [git_commands.md](../git/git_commands.md) 
  
    
    
  
  