FROM ubuntu:18.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server && \
    DEBIAN_FRONTEND=noninteractive apt-get clean

EXPOSE 6379

CMD ["redis-server", "--protected-mode no"]
