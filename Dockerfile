FROM python:3.9

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY train.py /code/train.py
ENTRYPOINT ["python", "train.py"]
