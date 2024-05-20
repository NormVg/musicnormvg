from flask import Flask,send_file,request,jsonify,redirect
from flask_cors import CORS

import manager

app = Flask(__name__)
CORS(app)

from pydrive2.auth import GoogleAuth
gauth = GoogleAuth()

@app.route("/",methods=["GET","POST"])
def login():
    a = gauth.GetAuthUrl()
    print(a)
    return redirect(a)

@app.route("/gg",methods=["GET","POST"])
def gg():
    code = request.args.get('code')
    
    gauth.Auth(code)
    gg = manager.get_file_list(parent="1f7V7JZ3_JJRCerPZ29ympK592A-hltla",gauth=gauth)
    
    
    return jsonify(gg)
# drive = GoogleDrive(gauth)


if __name__ == "__main__":
    app.run(debug=True,port=8080)