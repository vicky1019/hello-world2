# basic commands
- how to create Dockerfile

   `$ cd your project`
- basic instruction
    FROM
    RUN
    CMD
 -step\
  -creat a file named Dockerfile
    cd /Users/apple/PycharmProjects/git/python-notes
     
    `mkdir DockerFile_test`\
    `cd DockerFile_test/`\
    `touch Dockerfile`\
    `vim Dockerfile`\
    - FROM ubuntu
    - RUN apt-get update
    - CMD ["echo", "hello world...! from my first docker image"]

    `cat Dockerfile`(check the content in Dockerfile)\
    `docker build -t myimage:1.0 . ` \
    `waitting for building...`
  -after building
    `docker images` (check the you images)\
    `docker run your image id or your image name`\
    