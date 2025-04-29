# Use a base image with Python
FROM mcr.microsoft.com/devcontainers/python:0-3.10

# [Optional] Uncomment to install extra requirements
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# Install system dependencies you might need
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    apt-get install libgl1-mesa-glx