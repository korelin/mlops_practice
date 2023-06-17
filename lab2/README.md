# lab2

## Развертывание сервера Jenkins

1. Создать сетевой мост:
    ```bash
    docker network create jenkins
    ```
2. Чтобы обеспечить возможность запускать Docker in Docker скачать и запустить образ `docker:dind`:
    ```bash
    docker run \
      --name jenkins-docker \
      --rm \
      --detach \
      --privileged \
      --network jenkins \
      --network-alias docker \
      --env DOCKER_TLS_CERTDIR=/certs \
      --volume jenkins-docker-certs:/certs/client \
      --volume jenkins-data:/var/jenkins_home \
      --publish 2376:2376 \
      docker:dind \
      --storage-driver overlay2
    ```
3. Собрать Docker-образ Jenkins:
    ```bash
    docker build -t myjenkins-blueocean:2.401.1-1 -f Dockerfile_jenkins
    ```
4. Запустить контейнер из собранного образа `myjenkins-blueocean:2.401.1-1`:
```bash
docker run \
  --name jenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.401.1-1
```