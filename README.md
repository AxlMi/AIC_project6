# AIC_PROJECT6

## The purpose of this project is : 

  - Create a Dump of your database MYSQL and Zip
  - Save him on S3 bucket, all day in new folder with the corresponding date
  - Encrypt DATA with algorithm AES 
  - send mail to indicate the state of the script
  - Possibility to restore at the desirated date 
  - create Cron 

## install python3 : 

apt-get update
apt-get upgrade -y
apt-get install python3 python-pip3 git-all -y

## clone project : 

Use git clone https://github.com/AxlMi/AIC_project6

## create your virtual environment :

Install virtualenv : pip3 install virtualenv,
create your virtual environment : virtualenv -p python3 "name of your virtual environment"
active your virtual environment : source "name of yoour virtual environement"/bin/activate

## install the necessary modules :

you need to install, use : pip install -r requirements.txt

 ## Prerequisite :
 
 ### - Create/modify file confidential.py with this variable : 

 - aws_key = " enter ur AWS KEY, you can found him in your AWS Account"
 - aws_secret = " enter ur key secret , you can found him in your AWS Account"
 - sql_user = "enter ur account for use SQL"
 - sql_password = "enter ur password"
 - smtp_server = " indicate your smtp server"
 - smtp_port = "port of your smtp server"
 - user_smtp = " your mail address"
 - password_smtp " your password address"
 - fromaddr = " Systeme < your mail adress> "
 - toaddrs = " destination mail"
 - key_encryption = " your key AES " ( you can generate him with secure.py)
 
 
 ## VARIABLE : 
 
you can modify them in the file var.py , you need to indicate your bucket_name

 ## generate key_encryption :

for generate the key you can use python3 secure.py , this will create a file named "confidential.key", open the file and copy paste on confidential.py

## starting the script :

Now you can launch this script with : python3 main.py

this script will save all DB on your S3 bucket_name with this structruce : 

bucket_name\backup\"name of your server"\"name of your DB"

## Optionnal

If u want to recoverer DB on a date : use python3 sqlaws.py 

1) Indicates the name of the server
2) Indicate the Name of the DB you wish recoverer
3) Indicate the year of recovery in this format : 2020 
4) Indicate the month of recovery in this format : 01 for january or 12 for december
5) Indicate the day of recovery in this format : from 01 to 31

## Conclusion 

if you encounter any errors or difficulties,please do not hesitate to contact me.

you can also suggest me your areas for improvement by MP or pull request

Thanks for the reading
