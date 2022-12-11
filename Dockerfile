FROM python

WORKDIR /myapp

COPY * .

COPY templates templates/

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
