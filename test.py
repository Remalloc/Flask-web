#coding = utf-8
from flask_mail import Message
from hello import mail
from hello import app
msg = Message('test subject', sender='vbover@163.com',
recipients=['vbover@163.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)