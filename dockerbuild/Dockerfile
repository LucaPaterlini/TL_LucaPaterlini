FROM alpine
RUN apk add --update alpine-sdk
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk add libxml2-dev && apk add libxslt-dev && apk add python-dev
RUN apk add py-pip ; pip install --upgrade pip
RUN pip install lxml
RUN pip install pyquery
RUN pip install rfc3986 && apk add git
RUN git clone "https://github.com/LucaPaterlini/TL_LucaPaterlini.git" /home
RUN chmod +x /home/hackernews
RUN export PATH=$PATH":/home"
ENTRYPOINT ash -c "ash"