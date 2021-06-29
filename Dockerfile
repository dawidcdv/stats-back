FROM python:3.8-slim-buster

RUN mkdir -p /app && apt-get update && apt-get install -y dos2unix netcat
ENV PYTHONPATH=/app

COPY ["src","tests","requirements.txt", "entrypoint.sh", "./app/"]

RUN python3 -m pip install -r /app/requirements.txt
RUN chmod u+x /app/entrypoint.sh && dos2unix /app/entrypoint.sh && \
    chmod u+x /app/

WORKDIR /app/src
ENTRYPOINT  ["sh", "/app/entrypoint.sh"]

