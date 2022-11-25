FROM python:3.11.0-alpine3.16 as builder

WORKDIR /build

# install dependencies
RUN apk update
RUN apk add --no-cache gcc musl-dev postgresql-dev libffi-dev zlib-dev linux-headers g++ libev-dev libjpeg-turbo-dev

RUN pip3 install -U pip

COPY ./requirements.txt ./
RUN pip3 wheel \
		--no-cache-dir \
		--wheel-dir wheels \
		-r requirements.txt 

FROM python:3.11.0-alpine3.16

WORKDIR /usr/src/app

COPY --from=builder /build/wheels /wheels

RUN apk update
RUN apk add --no-cache libpq zlib curl libstdc++ libev libffi libjpeg-turbo
RUN apk upgrade

RUN pip install -U pip
RUN pip install --no-cache /wheels/*

COPY . /usr/src/app/

EXPOSE 8000