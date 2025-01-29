from flask import Flask,render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'swapnacvenu@gmail.com'
app.config['MAIL_PASSWORD'] = 'xymg xhus fjmp zlaq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/send_mail',methods=['POST'])
def send_message():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    message=request.form['message']
    msg = Message(subject='Hello', sender=email, recipients=['swapnacvenu@gmail.com'])
    msg.body = f"From: {name}\n {email}\n {phone}\nMessage:\n{message}"
    mail.send(msg)
    return render_template('index.html', success=True)

app.run()