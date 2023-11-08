from flask import Flask ,render_template,request,redirect
from flask_mail import Mail,Message
app=Flask(__name__)
app.secret_key ="Rahul"
# ----------------------------------------------------mail-----------------------------------------------------------------
app.config['SECRET_KEY'] = 'Rahul'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rahulsinghpal2001@gmail.com'
app.config['MAIL_PASSWORD'] = 'osucgwcwhjvoutsz'

mail=Mail(app)

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/contact", methods=['Post'])
def con():
    if request.method=="POST":
        name=request.form['nam']
        email=request.form['emal']
        Comt=request.form['msgs']
        msg = Message(
        'Thanks For Contacting !',
        sender='rahulsinghpal2001@gmail.com',
        recipients=[email,'paalrahul2001@gmail.com'] ,
        body=f'Hey {name},\n{Comt}\n\nWill Right Back As Soon As Possible\nThank You\n Rahul'
    )
        mail.send(msg)
        sdd="Thanks You"
    
    return  redirect("/")
