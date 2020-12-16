import csv
import pprint
from io import StringIO
from flask import render_template, redirect, request
from werkzeug.wrappers import Response

from app import app



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = [request.form.get('q{}'.format(i)) for i in range(1,50)]
        pprint.pprint(data)
        with open('data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        return redirect('/')
    return render_template('index.html')

@app.route('/download')
def download():
    def generate():
        with open('data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield ','.join(row) + '\n'
    return Response(generate(),
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=data.csv"})
