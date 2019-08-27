FROM python:alpine
#COPY /Simulator-Frontend /usr/share/nginx/html
#FROM python:alpine
RUN pip install pipenv
# They will be served by Nginx directly, without being handled by uWSGI
#ENV STATIC_URL /tmp/Simulator-Frontend
# Absolute path in where the static files wil be
#ENV STATIC_PATH /tmp/Simulator-Frontend
# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
#ENV STATIC_INDEX 1
ADD / home
#RUN cd /home/Simulator-Backend && 
WORKDIR /home/Simulator-Backend

RUN pipenv install --ignore-pipfile

CMD ["pipenv", "run", "python3", "Main.py"])