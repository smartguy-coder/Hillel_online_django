FROM python:3.8-alpine3.13

WORKDIR ./

RUN pip install --upgrade pip

COPY ./ ./

RUN pip install -r requirements.txt


ENTRYPOINT ["python", "manage.py"]
CMD  ["runserver", "0.0.0.0:8000"]
