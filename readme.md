## Table of Contents
- [CS1010X](#cs1010x)
- [Getting Started using Docker](#getting-started-using-docker)
    * [Prerequisites](#prerequisites)
    * [Clone With Git](#clone-with-git)
- [Working with Python on Docker and Intellij](#working-with-python-on-docker-and-intellij)

## CS1010X
My repo for CS1010X stuff.

## Getting Started using Docker

Quickstart guide to getting Docker-based dev environment up and running.

### Prerequisites

You need Docker installed. Use native version for your OS - use Toolbox only as last resort.
- Docker for Windows (preferred)
- Docker for Mac (preferred)
- Docker Toolbox

To run .sh scripts in a Windows environment, use Git Bash.

### Clone With Git

Do this step if you're starting fresh.

```
https://github.com/khoo0030/cs1010x.git
```

### Start Docker Containers
There are 2 services in the docker compose file

| Services | App | Exposed Port | Remarks |
| --- | --- | --- | --- |
| web | Nginx | 8080 | Access on http://localhost:8080 |
| app | Python | | |


Run docker compose

cd into the project root folder and run:

```
docker-compose up -d
```

### Working with Python on Docker and Intellij
Open project in Intellij
```
Install Python plugin 
```
```
alt-ctrl-shift s, project structure window will open
- Platform SDKs > add python SDK > select docker > add docker service containing python image
- Project settings > projects > select remote python interpreter
- Project settings > modules > select remote python interpreter
```
