FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD ./textteaser/requirements.txt  /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
ADD . /usr/src/app

RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"