from appname import app

@app.route('/')
def hello():
    return "Okay!"
    