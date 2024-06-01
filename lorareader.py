from flask import Flask, request, jsonify, render_template
import json
import struct

app = Flask(__name__)

def read_safetensor(file):
    try:
        length_of_header = struct.unpack('<Q', file.read(8))[0]
        header_data = file.read(length_of_header)
        header = json.loads(header_data)
        return header, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        header, error = read_safetensor(file)
        if error:
            return jsonify({'error': error}), 400
        return jsonify(header)
    return jsonify({'error': 'Unknown error'}), 400

if __name__ == '__main__':
    app.run(debug=True)


