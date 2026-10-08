from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ramas')
def ramas():
    return render_template('ramas.html')

@app.route('/empleos')
def empleos():
    return render_template('empleos.html')

if __name__ == '__main__':
    app.run(debug=True)
