FROM python:3.8

WORKDIR /backend

COPY ./requirements.txt /backend

RUN pip install --no-cache-dir --requirement /backend/requirements.txt

COPY . /backend

EXPOSE 5000

CMD [ "python","app.py"]
