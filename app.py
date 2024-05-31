from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    original_text = data.get('text')
    reversed_text = original_text[::-1]
    return jsonify({'reversed_text': reversed_text})

if __name__ == '__main__':
    app.run(debug=True)
