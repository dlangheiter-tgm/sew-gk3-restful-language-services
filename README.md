# SEW5 GK3 Restful Languege Service

## Setup environment
To install all required packages run:
```shell script
pip install -r requirements.txt
```

#### Required packages
* **PyQt5** for the ui on the client
* **pycld2** for the language detection (py compact language detector)
* **web.py** for the rest api/server

## Server
To start the server run:
```shell script
python src/server/Server.py
```
This starts the server and listens on the port `8080`.

It listens to GET requests to '/' with the GET parameter `text`.

## Client
To start the client run:
```shell script
python src/client/Client.py
```
This starts the ui client program.