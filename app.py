from flask import Flask, render_template, request, redirect, url_for
import json
import os
import uuid

app = Flask(__name__)
DATA_FILE = 'domains.json'

def load_domains():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_domains(domains):
    with open(DATA_FILE, 'w') as f:
        json.dump(domains, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        local = request.form['local']
        public = request.form['public']

        domains = load_domains()
        domains.append({
            'id': str(uuid.uuid4()),
            'name': name,
            'local': local,
            'public': public
        })
        save_domains(domains)
        return redirect('/')

    domains = load_domains()
    return render_template('index.html', domains=domains)

@app.route('/delete/<id>', methods=['POST'])
def delete_domain(id):
    domains = load_domains()
    domains = [d for d in domains if d.get('id') != id]
    save_domains(domains)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
