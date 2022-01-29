import yagmail
import os 

sender ='ajibadesegun94@gmail.com'
reciever = 'hqjvtocxd@emltmp.com'

subject = 'Studing for an interview'

contents = """
This is the content of the emai
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=reciever, subject=subject, contents=contents)
print('Email Successfully sent!')