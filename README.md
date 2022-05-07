# Techella

# Installation

## Install docker
### Windows
Run ```wsl --install``` in powershell with admin privileges
Download Docker from official website and follow instructions: [link](https://docs.docker.com/desktop/windows/install/)

### Linux
On linux you need to install docker package and then start docker service
#### Ubuntu
```
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
```
Start docker automaticaly if you want to:
```
sudo systemctl enable docker
````

#### Arch
Refer to [Arch Wiki](https://wiki.archlinux.org/title/Docker) if problems occur.
```
sudo pacman -S docker
sudo systemctl start docker.service
```
Start docker automaticaly if you want to:
```
sudo systemctl enable docker
````

#### Gentoo
Refer to [Gentoo Wiki](https://wiki.gentoo.org/wiki/Docker#Installation) if problems occur.
```
sudo emerge --ask --verbose app-containers/docker app-containers/docker-cli
sudo rc-update add docker default
sudo rc-service docker start
```
## Starting
Clone repository using [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
```
git clone https://github.com/Vring/FinalProject.git
cd FinalProject
```
And start all containers using ```docker compose```
```
docker compose up -d
```
-d option is used to run docker in background

# Docker commands
Run using ```docker compose```
```
docker compose up -d
```

Stop all containers
```
docker compose stop
```

Rebuild all containers
```
docker compose up -d --build
```

Or you can rebuild a single container:
```
docker-compose up -d --build [container-name]
```
Container names:
  - frontend
  - backend
  - scheduler
  - redis

More documentation is available at [Docker Docs](https://docs.docker.com/compose/).
