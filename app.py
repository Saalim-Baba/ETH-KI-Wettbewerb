from flask import Flask, request, jsonify, send_from_directory
import subprocess
import sys
import os
import json

app = Flask(__name__, static_folder='public')
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/execute', methods=['POST'])
def execute_script():
    script_path = os.path.join(os.path.dirname(__file__), 'message.py')
    argument_json = json.dumps((request.json)["array"])
    result = subprocess.run([sys.executable, script_path, argument_json], 
                            capture_output=True, 
                            text=True)
    output = result.stdout.strip()
    if output == None:
        print("fail")
    print("2" + output + "2")
    return output

if __name__ == '__main__':
    app.run(debug=True)
