FROM python:latest
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["gunicorn"  , "--bind", "0.0.0.0:5003", "app:app"]
