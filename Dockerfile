FROM --platform=linux/x86_64 python:3.11.4-alpine3.18

RUN pip install poetry==1.5.1

# A locale needs to be installed and set for later use by some python packages like click
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Store all of the packages under the /usr/src/app/ directory
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

# We turn off virtual env as not needed inside the container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the code into the image
COPY . .

EXPOSE 8000
