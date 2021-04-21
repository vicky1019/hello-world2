# building an image on GCP
## pick compute engine and build a vm instance
- select an OS according to your request\
- click SSH to bring up the connection
## build an image in the terminal of GCP
- cd to your project\
  follow `docker_relevent.md`
  
- after building an image\
  `$ls`(check the files on the current path)\
  `$ls /usr/bin/python*`(check python version)\
  `$ls -l /usr/bin/ | grep python`(check the soft connection)\
  (results are as followed)\
  ...\
  lrwxrwxrwx 1 root root           31 Mar 26  2019 py3versions -> ../share/python3/py3versions.py\
  lrwxrwxrwx 1 root root            9 Mar 26  2019 python3 -> python3.7\
  -rwxr-xr-x 2 root root      4877888 Jan 22 20:04 python3.7\
  -rwxr-xr-x 2 root root      4877888 Jan 22 20:04 python3.7m\
  lrwxrwxrwx 1 root root           10 Mar 26  2019 python3m -> python3.7m\
  ...
  
  

  
  


  
