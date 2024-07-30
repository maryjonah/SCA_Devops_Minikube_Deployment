FROM python:3.10-slim-bullseye

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5003
CMD ["python", "/app/main.py"]
