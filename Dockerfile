# Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip


# Copy project
COPY . /app/

# build dependencies
RUN apk add --no-cache --virtual .build-deps build-base libffi-dev postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# install required packages/scripts
RUN apk add --no-cache libpq openssl jq curl
# RUN wget -O /usr/local/bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/master/wait-for \
#     && chmod +x /usr/local/bin/wait-for

RUN openssl req -nodes -x509 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt \
    -outform PEM -days 7200 -subj "/CN=sre_reports/C=US/ST=WA/L=Somewhere City/O=Self-Signed Inc."

RUN pip install -r requirements.txt