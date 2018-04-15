
FROM ubuntu:16.04
MAINTAINER Manoj Joshi <manjoshi@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    git-core \
    wget \
    pandoc \
    default-jre \
    libssl-dev -y

# install net tools
RUN pip install netifaces
RUN git clone https://github.com/cloudmesh-community/hid-sp18-408.git


WORKDIR /hid-sp18-408/swagger-docker

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

EXPOSE 8080

RUN make service

CMD ["make", "start"]
