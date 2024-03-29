FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Musica
WORKDIR /Musica
COPY requirements.txt /Musica/
RUN pip install -r requirements.txt
COPY . /Musica/
CMD sudo python manage.py runserver --settings=settings.production 0.0.0.0:8080