from google/cloud-sdk

RUN apt-get update && apt-get install -y python3-dev python3-pip
RUN python3 --version

RUN pip3 install pygcloud


