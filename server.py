from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/menu/')
def menu():
  return render_template('menu.html')

@app.route('/reports/')
def reports():
  return render_template('reports.html')

@app.route('/index/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
  