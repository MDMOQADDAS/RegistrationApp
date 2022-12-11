FROM python

WORKDIR /myapp

COPY * /myapp/

COPY templates/myapp/templates/


RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
