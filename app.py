from flask import Flask
from flask import make_response,jsonify

app = Flask(__name__)

@app.route('/get',methods=["GET"])
def get_request():
    return make_response(jsonify({"name":"saikiran","age":26}),200)

@app.route('/signer')
def get_signed():
    return make_response(jsonify({"name":"saikiran","age":26,"auth":False,"isvaliduser":True}),202)

if __name__ == "__main__":
    app.run()