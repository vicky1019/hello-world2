# basic commands
- how to create Dockerfile

   `$ cd your project`
- basic instructions\
    FROM\
    RUN\
    ADD\
    ENV\
    CMD\
    EXPOSE
 ## step
  - creat a file named Dockerfile and building docker image \
    `cd /Users/apple/PycharmProjects/git/python-notes`\
    `mkdir DockerFile_test`\
    `cd DockerFile_test/`\
    `touch Dockerfile`\
    `vim Dockerfile`
    - FROM ubuntu (images, you can get from docker hub)
    - RUN apt update && apt upgrade
    - CMD ["echo", "hello world...! from my first docker image"]

    `cat Dockerfile`(check the content in Dockerfile)\
    `docker build -t myimage:1.0 . ` \
    waiting for building...
    
  - after building \
    `docker images` (check how many images that you have,decide whether you may delete some one)\
    `docker inspect [image ID|image name]`(get the details about the image in a json file)\
    $ docker inspect pii_us 
    `docker rmi -f [image ID]`\
    $ docker rmi `docker images -q`\
    $ docker rm `docker ps -a -q`\
    `docker ps -a"`(check processing container id info, -a: all the container)\
    `docker stop [container ID]`(stop the processing container)\
    `dcoker kill [container ID]`(force to stop container by container id)
    
  - running a docker image \
    `docker run [image ID|image name]`(return a id)
    
  - enter the container\
    `docker exec it [id] /bin/sh`(enter the container by id, the id is docker run returned id)
    