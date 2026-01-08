* Dockerfile → builds IMAGE
* IMAGE → run as CONTAINER
* docker-compose.yml → runs MULTIPLE containers

* RUN apk add --no-cache gcc musl-dev linux-headers
    * Installs Linux build tools
    * Required because:
        * Some Python packages (like redis) compile native extensions
        * --no-cache keeps the image smaller

* COPY requirements.txt. 
    * Copies requirements.txt from your machine → container
    * Done before copying app code for better Docker caching

* COPY . .
    * Copies **all project files** into the container
    * This includes:
        * app.py
        * Any other Python files
    * Without this → your app wouldn’t exist inside Docker

* services: Defines multiple containers that form one application.
    * web service: this is the flask app
        * build .: tell Docker Compose to build an image using the Docker File in this folder

* ports 5000:8000: port mapping
    * Browser → localhost:8000
    * Docker forwards → container port 5000
    * Flask listens on 5000

| Concept        | Meaning                                   |
| -------------- | ----------------------------------------- |
| Dockerfile     | How to build **one image**                |
| Image          | Blueprint                                 |
| Container      | Running instance                          |
| docker-compose | How **multiple containers** work together |
| Service name   | Internal DNS hostname                     |
