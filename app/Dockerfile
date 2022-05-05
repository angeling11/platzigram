FROM python:3.9.7-alpine3.14

# working directory
WORKDIR /app

# environment variables
# - prevents python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# - prevents python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install os packages
RUN apk update \
    && apk add build-base py-pip jpeg-dev zlib-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
