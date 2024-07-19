from flask import Flask, render_template, request
import os
from file_organizer import organize_files

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize():
    directory = request.form['directory']
    message = organize_files(directory)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
