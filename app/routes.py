from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Aleksander Ziętkiewicz!"

@app.route('/name/',defaults={'name': "Anonim"})
@app.route('/name/<name>')
def name(name=None):
    return f"Hello, {name}!"