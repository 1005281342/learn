FROM python:3.6
FROM taoliu/gunicorn3


WORKDIR /code

RUN pip3 install --upgrade pip

ADD ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

ADD . /code

EXPOSE 6668
CMD gunicorn api_sanic_docker:app --bind 0.0.0.0:6668 --worker-class sanic.worker.GunicornWorker -w=3 --threads=5  --timeout=600