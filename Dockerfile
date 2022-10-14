FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /opt/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    jpeg-dev zlib-dev libjpeg libxml2-dev libxslt-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /opt/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

WORKDIR /opt

EXPOSE 8000
CMD ["./start.sh"]

ADD . /opt
RUN chmod 755 /opt/start.sh
