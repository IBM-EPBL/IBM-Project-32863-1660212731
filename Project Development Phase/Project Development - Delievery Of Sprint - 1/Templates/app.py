from flask import flask
app= flask(__name__)
@app.route("/")
def WELCOME():
    return "Welcome to IBM !!!"

if __name__=="main":
    app.run()