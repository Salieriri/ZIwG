FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --requirement requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
