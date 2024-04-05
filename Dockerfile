FROM python:3.10.9

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install -r /tmp/requirements.txt

COPY . /app

EXPOSE 6000

CMD ['uvicorn','main:app','--host','0.0.0.0','--port', 6000]