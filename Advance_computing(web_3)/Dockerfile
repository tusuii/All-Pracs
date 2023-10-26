# Practical 1... 
# Turn windows feature on/of > hyper-v & WSL2
# wsl --status 
# wsl --set-default-version 2
# https://learn.microsoft.com/en-us/windows/wsl/install
# docker run hyperledger/fabric-nodeenv

FROM ubuntu

RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    unzip \
    git \
    apt-utils \
    build-essential \
    gcc \
    g++ \
    make

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# OR if error in node installation uncoment below line
#RUN apt-get install -y nodejs

RUN apt-get install -y openjdk-11-jdk

RUN add-apt-repository ppa:ethereum/ethereum
RUN apt-get update -y
RUN apt-get install -y solc

RUN wget https://go.dev/dl/go1.21.3.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.21.3.linux-amd64.tar.gz
RUN rm go1.21.3.linux-amd64.tar.gz

RUN apt-get install -y \
    docker.io \
    libtool \
    libltdl-dev \
    libssl-dev \
    autoconf \
    automake \
    bison \
    libboost-all-dev \
    libgflags-dev \
    libprotobuf-dev \
    libleveldb-dev \
    libsnappy-dev \
    libsodium-dev \
    liblz4-tool

RUN service --status-all

# RUN curl -sSL https://raw.githubusercontent.com/hyperledger/fabric/master/scripts/bootstrap.sh | bash -s -- 2.2.0 1.4.9

# RUN git clone https://github.com/hyperledger/fabric.git 
# COPY ./fabric-binaries/ /usr/local/bin/
# RUN chmod +x /usr/local/bin/*

RUN apt-get clean                                  # can skip
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  # can skip

WORKDIR /app

CMD ["/bin/bash"]


# commands to run
# docker build .
# docker images
# docker container ls
# docker exec -it <hash> bash

