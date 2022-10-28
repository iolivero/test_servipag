FROM alpine
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip && python3 -m pip install --upgrade pip && pip3 install flask
RUN mkdir -p /home/apipython
COPY main.py /home/apipython/
EXPOSE 5000:5000
CMD python3 /home/apipython/main.py