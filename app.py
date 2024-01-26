import os
import subprocess
import json
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

app.config['ACCESS_TOKEN'] = '7pNpFt2aeG5RkmS3T6Yy'

# API endpoint to process the uploaded file with an executable
@app.route('/upload', methods=['POST'])
def process_file():
    token = request.args.get('access_token')

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    if token == app.config['ACCESS_TOKEN']:
        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if file:
            # Save the uploaded file
            current_datetime = datetime.datetime.now()
            timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(timestamp + "_" + file.filename))
            file.save(filename)

            subprocess.call(["/app/hayabusa/hayabusa-2.12.0-lin-x64-musl", "json-timeline", "-f", f"/app/{filename}", "-w", "-L", "-o", f"/app/{filename}.json"])

            try:
                with open(f"/app/{filename}.json", 'r') as f:
                    file_content = [json.loads(line) for line in f]
                    return jsonify(file_content), 200
            except:
                return jsonify({"error": "Something went wrong returning the hayabusa output"}), 500
    else:
        return jsonify({'error': 'Unauthorized access'}), 401
    

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, host="0.0.0.0")
