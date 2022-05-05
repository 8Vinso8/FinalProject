# Techella

# Installation

## Install docker
### Windows
Run ```wsl --install``` in powershell with admin privileges
Download Docker from official website and follow instructions: [link](https://docs.docker.com/desktop/windows/install/)

### Linux
On linux you need to install docker and docker-compose packages and then start docker service
#### Ubuntu
```
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Start docker automaticaly if you want to:
```
sudo systemctl enable docker
````

#### Arch
Refer to [Arch Wiki](https://wiki.archlinux.org/title/Docker) if problems occur.
```
sudo pacman -S docker docker-compose
sudo systemctl start docker.service
```
Start docker automaticaly if you want to:
```
sudo systemctl enable docker
````

#### Gentoo
Refer to [Gentoo Wiki](https://wiki.gentoo.org/wiki/Docker#Installation) if problems occur.
```
sudo emerge --ask --verbose app-containers/docker app-containers/docker-cli app-containers/docker-compose
sudo rc-update add docker default
sudo rc-service docker start
```
## Starting
Clone repository using [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and start docker
```
git clone https://github.com/Vring/FinalProject.git
cd FinalProject
docker-compose up -d
```
