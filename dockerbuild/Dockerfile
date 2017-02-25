FROM alpine

RUN apk --update add \
    libc-dev \
    gcc \
    git \
    libxml2-dev \
    libxslt-dev \
    python \
    python-dev \
    py-pip

RUN pip install --upgrade pip \
    lxml \
    pyquery \
    rfc3986

RUN git clone "https://github.com/LucaPaterlini/TL_LucaPaterlini.git" /tmp/hackernews \
    && cp /tmp/hackernews/hackernews_lib/ -r /usr/lib/python2.7/ \
    && cp /tmp/hackernews/hackernews /usr/bin \
    && chmod +x /usr/bin/hackernews \
    && rm -Rf /tmp/hackernews

ENTRYPOINT ash -c "ash"