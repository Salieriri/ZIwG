FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --requirement requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]

# CMD cd Dataflow && \
#     scrapy crawl eurogamer -o data/Eurogamer.json && \
#     scrapy crawl gryonline -o data/GryOnline.json && \
#     scrapy crawl ppe -o data/PPE.json && \
#     cd .. && \
#     python ZipWithData/main.py data . Eurogamer GryOnline PPE
