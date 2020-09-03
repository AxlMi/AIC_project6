# AIC_PROJECT6

## The purpose of this project is : 

  - Create a Dump of your database MYSQL
  - Save him on S3 bucket, all day in new folder with the corresponding date
  - Encrypt DATA with algorith AES 
  - send mail to indicate the state of the script
  - Possibility to restore at the desirated date 
 
 ## FOR USE u need :
 
  - Create file confidential.py with this variable : 
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
                                                      - key_encryption = " your key AES"
                                                      
