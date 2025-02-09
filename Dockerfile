FROM python:3.12-slim

ENV APP_DIR /app

# RUN adduser -D quart
WORKDIR /app

COPY requirements-freeze.txt ./requirements.txt
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze > requirements-freeze.txt

COPY ./app .
COPY ./run.py .

# USER quart
EXPOSE 5000

CMD ["uvicorn", "run:create_app", "--factory", "--host=0.0.0.0", "--port", "5000", "--reload", "--proxy-headers"]
