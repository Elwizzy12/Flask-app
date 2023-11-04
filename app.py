from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/template')
def template_example():
    return render_template('template.html')

@app.route('/json')
def json_example():
    data = {'message': 'Hello, JSON!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)