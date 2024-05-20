from flask import Flask,send_file,request,jsonify,redirect
from flask_cors import CORS
from pydrive2.auth import GoogleAuth

import manager

app = Flask(__name__)
CORS(app)

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

