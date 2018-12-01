FROM alpine:edge

WORKDIR /tmp
COPY requirements.txt .

RUN apk add --update --no-cache --virtual=build-dependencies \
    gcc \
    libc-dev \
    libxml2-dev \
    libxslt-dev \
    python3-dev \
  && apk add --no-cache \
    libxml2 \
    libxslt \
    python3 \
  && python3 -m pip install -r requirements.txt \
  && apk del --purge build-dependencies \
  && rm -rf /tmp/*

WORKDIR /data
COPY . .
