from flask import Flask,render_template,request
from pymongo import MongoClient
import subprocess as sp
import os

mongo_server_url="mongodb://127.0.0.1:27017"
client = MongoClient(mongo_server_url)

app = Flask("chat app")
#here i am going to defind database and collection name
db ="lw"
collection="flask"

#We have to specify that In which IP and port you want to run this web app
port=80
hostname="0.0.0.0"


@app.route('/')
def home():
    #Very Important steps
    file=open("names.yml" , "r+")
    file.truncate(0)
    file.close()
    file=open("mobiles.yml" , "r+")
    file.truncate(0)
    file.close()
    file=open("emails.yml" , "r+")
    file.truncate(0)
    file.close()
    return render_template("index.html")

@app.route('/sumbitted' , methods=['POST'])
def sumbitted():
    name=request.form.get("name") 
    mobile=request.form.get("mobile")
    email=request.form.get("email")
    #inserting the data in mongodb server
    client[db][collection].insert({"name": name , "mobile": mobile , "email": email})
    #now i want to do some manupulation to store the name, mobile and email 
    
    # file handling for "names.yml"
    f = open("names.yml" ,"a")
    var="moqaddas"
    f.write("name: ")
    f.write(name)
    f.close()

    # file handling for "mobiles.yml"
    f = open("mobiles.yml" ,"a")
    var="moqaddas"
    f.write("mobile: ")
    f.write(mobile)
    f.close()

    # file handling for "names.yml"
    f = open("emails.yml" ,"a")
    var="moqaddas"
    f.write("email: ")
    f.write(email)
    f.close()
   

    m=sp.getstatusoutput("ansible-playbook mail.yml  --vault-password-file password.txt")
    exit_code=m[0]
    output=m[1]
    if exit_code==0:
        
        

        return render_template("response.html")
    else: return render_template("err.html")
    
app.run(debug=True , port=port , host=hostname)
