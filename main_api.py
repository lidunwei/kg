# -*- coding: utf-8 -*-
import json
from flasgger import Swagger
from flask_cors import *
from config import Config
from flask import Flask, render_template, request
from src.data_handle import handle_main
from urllib.parse import unquote
app = Flask(__name__, template_folder='templates', static_folder='web', static_url_path='/web')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, suppors_credentials=True, resources={r'/*'})  # 设置跨域
swagger = Swagger(app)


@app.route('/api/data/kg', methods=['POST'])
def get_data():
    res = unquote(request.headers["Referer"], encoding="utf8")
    headers = str(res).split("?")[1].split("&")
    type = name = ''
    for element in headers:
        if "type" in element:
            type = element.replace("type=", "")
        else:
            name = element.replace("name=", "")
    data = handle_main(name, type)
    return json.dumps(data, ensure_ascii=False)


@app.route('/api/data/cycle', methods=['POST'])
def get_cycle():
    res = unquote(request.headers["Referer"], encoding="utf8")
    headers = str(res).split("?")[1].split("&")
    name = ''
    for element in headers:
        name = element.replace("name=", "")
    with open("data/" + name + "/cycle.json", encoding="utf8") as f:
        data = json.load(f)
    return json.dumps(data, ensure_ascii=False)


@app.route('/index')
def getHtml():
    return render_template('cycle.html')


@app.route('/kg')
def getKgHtml():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=Config.PYTHON_PORT)
