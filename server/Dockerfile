FROM python:3.8.5-slim-buster

LABEL version="1.0"
LABEL description="REST API server for the 2014 i2b2 dataset"
LABEL maintainer ""

ARG S6_VERSION
ENV S6_VERSION=${S6_VERSION:-v2.1.0.0}
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV PIP_NO_CACHE_DIR=off
ENV APP_USER=app
ENV APP_DIR=/opt/app

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Install dependencies
# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        curl \
        vim \
        unzip \
        openssl \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*
# Set up SSL cert
RUN  openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out server.pass.key
RUN  openssl rsa -passin pass:x -in server.pass.key -out server.key
RUN openssl req -new -key server.key -out server.csr \
        -subj "/C=US/ST=Wisconsin/L=Milwaukee/O=OrgName/OU=CTSI/CN=localhost" && \
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt


# Set up S6 init system
RUN curl -fsSL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
        -o /tmp/s6-overlay.tar.gz \
    && tar xzf /tmp/s6-overlay.tar.gz --directory / \
    && rm -fr /tmp/s6-overlay.tar.gz

RUN mkdir -p ${APP_DIR}/tools/

# Add app user
RUN useradd -m -s /bin/bash ${APP_USER} \
    && echo "${APP_USER}:${APP_USER}" | chpasswd

# Copy server files
COPY . ${APP_DIR}
RUN chown -R ${APP_USER}:${APP_USER} ${APP_DIR}

# Install dependencies
RUN pip install -r ${APP_DIR}/requirements.txt

# Add s6 scripts
COPY root /

EXPOSE 8080

ENTRYPOINT ["/init"]