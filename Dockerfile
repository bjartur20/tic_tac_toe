FROM python:3.10

WORKDIR /tic-tac-toe

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]
