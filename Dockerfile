FROM python

WORKDIR /myapp

COPY * /myapp/

CMD ["python3", "app.py"]
