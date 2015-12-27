from app import app, db

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/dbtest')
def dbtest():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return "It doesn't work"