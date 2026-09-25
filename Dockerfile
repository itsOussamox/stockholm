FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /stockholm

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    make \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash obouadel42 && \
    echo "obouadel42 ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY Makefile .
COPY src/args.py src/infection.py src/stockholm.py src/crypto.py src/
COPY infection/log.csv infection/Documents/lorem.doc infection/
COPY infection/album/tracklist.txt infection/album/theme.mp3 infection/album/Beethoven.jpg infection/album/

RUN cp -r infection /home/obouadel42/infection && \
    chown -R obouadel42:obouadel42 /home/obouadel42/infection && \
    chown -R obouadel42:obouadel42 /stockholm

USER obouadel42

CMD ["bash"]