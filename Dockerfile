FROM python:3.9-slim-bullseye
LABEL author="Mofiala Hervé LOKOSSOU hervlokossou@gmail.com"

ARG ARG_FLASK_ENV
ARG PYTHON_VERSION=python3

ENV FLASK_DEBUG $ARG_FLASK_ENV
# if --build-arg ARG_FLASK_ENV=1, set NODE_ENV to 'dev' or set to null otherwise.
ENV NODE_ENV=${ARG_FLASK_ENV:+dev}
# if NODE_ENV is null, set it to 'prod' (or leave as is otherwise)
ENV NODE_ENV=${NODE_ENV:-prod}

RUN echo "Executing in $NODE_ENV"

RUN python --version
RUN python -m pip install -U pip

RUN python -m pip config set global.trusted-host \
    "pypi.org files.pythonhosted.org pypi.python.org" \
    --trusted-host=pypi.python.org \
    --trusted-host=pypi.org \
    --trusted-host=files.pythonhosted.org


COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt

RUN chmod 777 /app

EXPOSE 5000
# This is the only known way to handle signals and use env vars simultaneously.
CMD exec python wsgi.py $NODE_ENV

