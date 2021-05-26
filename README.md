RegistrationApp
================ 
This is Flask and MongoDB based app

How App Look Like?
-----------------

### Here We have to put the details.
![image](https://user-images.githubusercontent.com/69861558/119587590-9bdfd080-bdec-11eb-9eab-48ba6a3de55b.png)

### After the details this page come up, if seat confirmed then you'll get a mail

![image](https://user-images.githubusercontent.com/69861558/119587670-c3cf3400-bdec-11eb-8df2-cb93409e5f5c.png)

### See this is a mail you'll get.
![image](https://user-images.githubusercontent.com/69861558/119587763-f842f000-bdec-11eb-9e52-935f73abc0ec.png)

### Now see if any client put wrong info then
![image](https://user-images.githubusercontent.com/69861558/119588343-3c82c000-bdee-11eb-86fb-28f4bade1db0.png)
![image](https://user-images.githubusercontent.com/69861558/119588359-460c2800-bdee-11eb-9e2c-ff7fceba6741.png)

### Now let's see the database all the data store in MongoDB or not?
![image](https://user-images.githubusercontent.com/69861558/119588777-1c073580-bdef-11eb-86d4-2278a74f2fbd.png)


Requirement
-----------
This app is a combination of three tools
#### Ansible
#### MongoDB
#### Flask
So just install above software in Linux Operationg System

Open the file<br><br>
**sudo vim password.txt**<br>
Putt the password for ansible-vault<br>

Open the file<br><br>
**sudo vim vault.yml**<br>
Putt the value as<br>
**gmail: gmail**<br>
**password: pass**<br>
Run below command<br>
**ansible-vault encrypt vault.yml --vault-password-file password.txt**

<br><br>
Open the file
**sudo vim app.yml**<br>
replace IP and port number<br>

![image](https://user-images.githubusercontent.com/69861558/119589496-853b7880-bdf0-11eb-82b3-e26a2fd9d504.png)

Create the mongodb database called **lw**<br>
Create the collections called **flask**<br>

You creat and db and collection names if you do this you have to change.
![image](https://user-images.githubusercontent.com/69861558/119589616-c6338d00-bdf0-11eb-8f52-813666a37a6c.png)

