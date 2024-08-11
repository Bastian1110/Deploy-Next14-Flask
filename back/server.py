# By Sebastian Mora (@Bastian1110)
from flask import Flask, request, jsonify, send_from_directory, send_file, abort
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='out')
CORS(app)

@app.route('/_next/static/<path:path>')
def serve_next_static(path):
    return send_from_directory(os.path.join(app.static_folder, '_next/static'), path)

@app.route('/static/<path:path>')
def serve_static_files(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    # Here you just need to add every of your routes :D
    if path == "miau":
        return serve_file_or_404('miau.html')
    
    return serve_file_or_404(path)

def serve_file_or_404(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        return send_file(os.path.join(app.static_folder, '404.html')), 404

@app.route('/', methods=['GET'])
def index():
    return send_file(os.path.join(app.static_folder, 'index.html'))

@app.errorhandler(404)
def page_not_found(e):
    return send_file(os.path.join(app.static_folder, '404.html')), 404

#Example route to test front-back interaction
@app.route("/ping", methods=["POST"])
def ping():
    try:
        data = request.get_json() 
        number = data["number"]
        print(f"Ping {number} received!")
        return jsonify({"message" : "Sucecess"}), 200
    except:
        print("Mega fail!")
        return jsonify({"message" : "Failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)