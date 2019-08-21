FROM python:alpine

RUN pip install pipenv

ADD / tmp

RUN cd /tmp/Simulator-Backend && pipenv install --ignore-pipfile

WORKDIR /tmp/Simulator-Backend

CMD ["pipenv", "run", "python3", "Main.py"]