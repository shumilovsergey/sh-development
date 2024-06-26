FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code

RUN pip3 install --upgrade pip

RUN pip3 install Django
RUN pip3 install django-tailwind
RUN pip3 install 'django-tailwind[reload]'

COPY . .

CMD python manage.py runserver 0.0.0.0:8000