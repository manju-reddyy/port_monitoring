# port_monitoring

Port Monitoring helps identify and close all the ports that are open in an security group in all of the aws accounts. 

Create a Lambda function using the port_monitoring.py file

#Attach an IAM role to the Lambda function:

In order to have access to modify the Security groups in other accounts, we need to attach an IAM role to the Lmabda function, so follow Lamda_role.docx file inorder to that.

#Create cloudwatch events

Inorder for the Lambda function to be triggered once in a day, create a cloudwatch alaram by following the steps in cloudwatch_role.docx
