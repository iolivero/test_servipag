FROM golang:1.14.2-alpine
WORKDIR /main
COPY . .
RUN go build .
RUN rm Dockerfile && rm main.go && rm Readme.md
CMD "./main"


