from flask import Flask
from flask import make_response,jsonify,request

app = Flask(__name__)

@app.route('/get',methods=["GET"])
def get_request():
    return make_response(jsonify({"name":"saikiran","age":26}),200)

@app.route('/signer')
def get_signed():
    return make_response(jsonify({"name":"saikiran","age":26,"auth":False,"isvaliduser":True,"authkey":"ckf439furcnkfehr8393xcjnsk","expiresin":"10m"}),202)

@app.route('/security')
def security_dispatch():
    return make_response(jsonify({"security":True,"enctype":"AES536","enc":"Military-Grade Encryption"}))

@app.route('/monitoring')
def monitor_logs():
    return make_response(jsonify({"monitor_type":"prometheus","log_store":"azure analytics workspace","dashboard_type":"grafana"}))

@app.route("/signature",methods=["POST"])
def validate_signature():
    if request.headers.get("Content-Type",None) == "application/json":
        return make_response(jsonify({"accepted":True,"user":"saikiran"}),200)
    else:
        return make_response(jsonify({"accepted":False,"user":"Unknown"}),303)

if __name__ == "__main__":
    app.run()