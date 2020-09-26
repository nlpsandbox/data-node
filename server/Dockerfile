FROM python:3.7.9-slim-buster

ARG S6_VERSION
ENV S6_VERSION=${S6_VERSION:-v1.21.7.0}
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV PIP_NO_CACHE_DIR=off

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

# Set up S6 init system
RUN curl -fsSL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
        -o /tmp/s6-overlay.tar.gz \
    && tar xzf /tmp/s6-overlay.tar.gz --directory / \
    && rm -fr /tmp/s6-overlay.tar.gz

# Add app user
RUN useradd -m -s /bin/bash app \
    && echo "app:app" | chpasswd

# RUN mkdir -p /etc/services.d/app
# COPY s6/app-run.sh /etc/services.d/app/run

# Copy server files
COPY requirements.txt /opt/app/
COPY openapi_server /opt/app/openapi_server/

RUN chown -R app:app /opt/app

# Install dependencies
RUN pip install -r /opt/app/requirements.txt

COPY root /

# Add s6 scripts
# COPY s6-scripts/configure-user.sh /etc/cont-init.d/10-configure-user
# COPY s6-scripts/get-dataset-files.sh /etc/cont-init.d/20-get-dataset-files

EXPOSE 8080

CMD ["/init"]