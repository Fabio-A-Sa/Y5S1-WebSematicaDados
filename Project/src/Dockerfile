FROM python:slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ARG APP_DIR
COPY ./${APP_DIR:?} ./${APP_DIR:?}
WORKDIR /app/${APP_DIR:?}

ARG APP_PORT
ENV APP_PORT=${APP_PORT:?}

EXPOSE ${APP_PORT:?}

CMD [ "/bin/sh", "-c", "flask run --host=0.0.0.0 --port=${APP_PORT} --debug" ]