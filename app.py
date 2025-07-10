
from flask import Flask, render_template, jsonify
from db_config import fetch_employees

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/employees')
def employees():
    data = fetch_employees()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
