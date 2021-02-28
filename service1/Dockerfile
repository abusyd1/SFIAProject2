FROM python:latest
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["gunicorn"  , "--bind", "0.0.0.0:5000", "app:app"]
