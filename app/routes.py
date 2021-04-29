from app import app

@app.route('/')
@app.route('/index.html')
def index():
    return "Index!"

@app.route('/login')
def login():
    return "<h1>Hello World!</h1>"
@app.route('/register')
def register():
    return "<h1>Stick register stuff here</h1>"

