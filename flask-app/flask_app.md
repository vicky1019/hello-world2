# create http api interface
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
  
- after install all the packages or dependencies\
    `$ pip freeze > requirements.txt`(auto-create requirements.txt，save this requirement and its dependencies so App Platform can install them later)
        
## 2. creating mini flask app
    here is an instance in app.py


## 3. setting up your gunicorn configuration
- what is gunicorn ?\
    Gunicorn is a Python WSGI(web server gateway interface) HTTP server that many developers use to deploy their Python applications\-
  
### steps
  - `$ touch gunicorn_config.py` Open a file named `gunicorn_config.py`
  - Pushing the Site to GitHub\
    `$ git init`\
    `$ touch .gitignore`(unnecessary file ignored)\
    add your files to your repository`$ git add app.py requirements.txt gunicorn_config.py .gitignore`\
    `$ git commit -m"initial Flask app"`\
    open your github, login your profile, and create a new repository called flask-app. create an empty repository without a README or license file,once you created the repository, return to the command line and push your local files to github\
    `$ git remote add origin https://github.com/your_usrname/flask-app` \
    rename the default branch main, to match what github expects:
    `$ git branch -M main`\
    `$ git push -u origin main` (push your main branch to github`s main branch)
    
    
  
  