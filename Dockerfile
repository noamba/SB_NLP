FROM tiangolo/uwsgi-nginx-flask:python3.6

# upgrade pip, copy requirements.txt and
# install required python packages from it
RUN pip install -U pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./app /app