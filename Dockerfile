FROM python

WORKDIR /myapp

COPY * .


RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
