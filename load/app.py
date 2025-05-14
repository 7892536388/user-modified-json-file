from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# Load JSON and show on form
@app.route('/', methods=['GET'])
def index():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return render_template('form.html', data=data)

# Save edited JSON
@app.route('/save', methods=['POST'])
def save():
    new_data = request.form.to_dict()
    with open(DATA_FILE, 'w') as f:
        json.dump(new_data, f, indent=4)
    return "JSON data saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
