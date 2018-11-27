FROM python:3.6
FROM taoliu/gunicorn3

ADD . /code
WORKDIR /code

RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements.txt

EXPOSE 6668
CMD gunicorn api_sanic_docker:app --bind 0.0.0.0:6668 --worker-class sanic.worker.GunicornWorker -w=3 --threads=5  --timeout=600