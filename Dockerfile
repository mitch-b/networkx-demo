FROM python:3.11-slim

WORKDIR /graphapp

COPY ./requirements.txt /graphapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /graphapp/requirements.txt

COPY ./app /graphapp/app

# Expose the port on which the application will run
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
