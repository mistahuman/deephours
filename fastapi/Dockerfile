FROM python:3.13-slim

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

COPY app /code/app
COPY .env.production /code/.env
COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt gunicorn

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "app.main:app"]
