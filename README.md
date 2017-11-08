# houseTemperature
Flask App to track house temperature



```bash
tree -I "venv|__pycache__|target" 
── Dockerfile
├── README.md
├── build.py
├── build_template_flask.sh
├── now.json
├── requirements.txt
├── run.py
└── src
    ├── main
    │   ├── python
    │   │   └── houseTemperature
    │   │       ├── __init__.py
    │   │       ├── app.py
    │   │       ├── controllers
    │   │       │   ├── __init__.py
    │   │       │   ├── home.py
    │   │       │   ├── temperature.py
    │   │       │   └── zoegs.py
    │   │       ├── models
    │   │       │   ├── __init__.py
    │   │       │   ├── home.py
    │   │       │   ├── tempKey.json
    │   │       │   └── temperature.py
    │   │       ├── run.py
    │   │       ├── static
    │   │       └── templates
    │   │           ├── base.html
    │   │           ├── home.html
    │   │           └── zoegs.html
    │   └── scripts
    └── unittest
        └── python
            └── test.py
```

## Package
I am using the pybuilder package to manage the building and testing. Simply run the below in the root directory to build.
```bash
pyb
```

## Dockerise

** Build the Docker image from the Dockerfile **

Running this cmd from the root:
```commandline
docker build -t housetemperature .
```

Runnning the server from the Docker file
```commandline
docker run -it --name tempRunner -p 5000:5000 housetemperature
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

