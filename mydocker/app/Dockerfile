FROM fedora:latest
RUN dnf -y update
RUN dnf -y install python

COPY . /opt/source-code

CMD ["python","/opt/source-code/hello.py"]