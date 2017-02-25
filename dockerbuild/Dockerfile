FROM alpine

RUN apk --update add \
    libc-dev \
    gcc \
    git \
    libxml2-dev \
    libxslt-dev \
    python-dev \
    py-pip

RUN pip install --upgrade pip \
    lxml \
    pyquery \
    rfc3986

RUN git clone "https://github.com/LucaPaterlini/TL_LucaPaterlini.git" /tmp/hackernews

RUN cp tmp/hackernews/hackernews_lib/ /usr/lib/python2.7/ -r
RUN cp tmp/hackernews/hackernews_tests/ /usr/lib/python2.7/ -r
RUN cp tmp/hackernews/hackernews /usr/bin
RUN chmod +x /usr/bin/hackernews \
    && rm -Rf /tmp/hackernews


ENTRYPOINT ash -c "ash"