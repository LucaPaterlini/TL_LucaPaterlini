#!/usr/bin/env bash

apt-get update
apt-get install   libc6-dev gcc git libxml2-dev libxslt1-dev python-dev
apt-get -y install python-pip

pip install lxml pyquery rfc3986
