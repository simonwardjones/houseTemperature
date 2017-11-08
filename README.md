# dsToolbox
Flask App for the Data Science team

#### Todo:
- [x] Built Template 
- [x] Add virtual env and freeze requirements
- [x] Add pybuilder
- [x] Dockerise
- [ ] Deploy


```bash
tree -I "venv|__pycache__|target" 

.
├── Dockerfile
├── README.md
├── build.py
├── build_template_flask.sh
├── now.json
├── requirements.txt
├── run.py
└── src
    ├── main
    │   ├── python
    │   │   └── dsToolbox
    │   │       ├── __init__.py
    │   │       ├── app.py
    │   │       ├── controllers
    │   │       │   ├── __init__.py
    │   │       │   ├── home.py
    │   │       │   └── ngrams.py
    │   │       ├── models
    │   │       │   ├── __init__.py
    │   │       │   └── home.py
    │   │       ├── run.py
    │   │       ├── static
    │   │       └── templates
    │   │           ├── base.html
    │   │           ├── home.html
    │   │           └── ngrams.html
    │   └── scripts
    └── unittest
        └── python
```

#### N-grams page
- Upload csv with column named Comments. N-grams is calculated with the column

## Package
I am using the pybuilder package to manage the building and testing. Simply run the below in the root directory to build.
```bash
pyb
```

## Dockerise

** Build the Docker image from the Dockerfile **

Running this cmd from the root:
```commandline
docker build -t dstoolbox .
```
Runnning the server from the Docker file
```commandline
docker run -it --name dsToolBoxRunner -p 5000:5000 dstoolbox
```

check it is running:
```commandline
docker ps
```
Note this just just shows the runnin ones, to see all use
```commandline
docker ps -a
```
To delete all containers us this (q restricts the sub cmd to give just ids)
```commandline
docker rm $(docker ps -a -q)
```

Or use this to get rid of the exited ones:
```commandline
$ docker rm -f "filter=excited"
```

