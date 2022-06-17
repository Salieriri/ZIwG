FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -i https://pypi.clarin-pl.eu/ lpmn_client

ENTRYPOINT ["tail", "-f", "/dev/null"]
