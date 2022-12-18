FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/hello.py python