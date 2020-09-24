FROM python:3.7.9-slim-buster

ARG S6_VERSION
ENV S6_VERSION=${S6_VERSION:-v1.21.7.0}
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Install dependencies
# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        curl \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

# RUN mkdir -p /usr/src/app
# RUN mkdir -p /usr/src/init

# COPY server /usr/src/app
# COPY init /usr/src/init
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

## Set up S6 init system
RUN curl -fsSL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
        -o /tmp/s6-overlay.tar.gz \
    && tar xzf /tmp/s6-overlay.tar.gz --directory / \
    && rm -fr /tmp/s6-overlay.tar.gz

# Install dependencies
# hadolint ignore=DL3008
# RUN apt-get update -qq -y \
#     && apt-get install --no-install-recommends -qq -y \
#         supervisor \
#     && apt-get -y autoclean \
#     && apt-get -y autoremove \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip3 install --no-cache-dir supervisor==4.2.1
# RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# WORKDIR /usr/src/app

EXPOSE 8080

# CMD ["/usr/bin/supervisord"]

CMD ["/init"]