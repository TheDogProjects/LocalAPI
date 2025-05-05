import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/localapi/cmd/<string:command>', methods=['POST'])
def execute_command(command):
    if not zmienna:
        return jsonify({"error": "Command Required"}), 400

    try:
        os.system(command)
        return jsonify({"message": f"Executed: {command}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
