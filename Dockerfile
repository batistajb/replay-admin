FROM python:3.12.6-slim

ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONFAULTHANDLER 1 # Makes Python more verbose in case of an error
ENV PIPENV_VENV_IN_PROJECT 1

RUN pip install pipenv

RUN useradd -ms /bin/bash replay

USER replay

WORKDIR /home/replay/app

COPY . .

CMD ["./start.sh"]