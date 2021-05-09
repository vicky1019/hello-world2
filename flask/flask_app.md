# create http api interface
## 1.create a new virtual env
- conda manage virtual env\
    `$conda env list`(check the current env list)\
    `$conda create -n py38 python==3.8`(create your virtual env named py38)\
- activate your env\
    in your interpreter(if you are using pycharm, in settings->project->project interpreter-> add->conda environment)\
    or in command line click `$activate py38`(activate your env)\
- install some packages\
    `$ pip install -i http:---(domestic image)`\
    `$ pip list or pip freeze`(check whether you have installed the packages)\
        
## flask framework
    here is an instance in app.py\ 