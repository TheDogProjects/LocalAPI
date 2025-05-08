from datetime import datetime
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import multiprocessing


RULESACCEPT = True

if RULESACCEPT == True:

    app = Flask(__name__)
    CORS(app)

    @app.route('/localapi/cmd/<string:cmd>', methods=['POST'])
    def execute_command(cmd):
        if not cmd:
            return jsonify({"error": "Add cmd Parameter"}), 400

        try:
            os.system(zmienna)
            return jsonify({"message": f"Executed: {cmd}")
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @app.route('/localapi/log/<string:txt>', methods=['POST'])
    def log(txt):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        print(f"\033[32m[LOG]\033[37m \033[37m[\033[34m{hour}:{minute}:{second}\033[37m] {txt}")
        return (f"API REQUEST SENT SUCCESSFULLY at \033[37m[\033[34m{hour}:{minute}:{second}\033[37m]")
    

    @app.route('/localapi/warn/<string:txt>', methods=['POST'])
    def warn(txt):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        print(f"\033[33m[WARN]\033[37m \033[37m[\033[34m{hour}:{minute}:{second}\033[37m] {txt}")
        return (f"API REQUEST SENT SUCCESSFULLY at \033[37m[\033[34m{hour}:{minute}:{second}\033[37m]")
    
    @app.route('/localapi/err/<string:txt>', methods=['POST'])
    def err(txt):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        print(f"\033[31m[ERROR]\033[37m \033[37m[\033[34m{hour}:{minute}:{second}\033[37m] {txt}")
        return (f"API REQUEST SENT SUCCESSFULLY at \033[37m[\033[34m{hour}:{minute}:{second}\033[37m]")
    
    @app.route('/localapi/info/cpu/cores', methods=['GET'])
    def get_info():
        return str(multiprocessing.cpu_count())


    if __name__ == '__main__':
        app.run(debug=True)

else:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    print(f"\033[31m[ERROR] \033[37m[\033[34m{hour}:{minute}:{second}\033[37m] Accept The Rules")
