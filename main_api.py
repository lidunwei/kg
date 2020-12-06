# -*- coding: utf-8 -*-
import json
from flasgger import Swagger
from flask_cors import *
from config import Config
from flask import Flask, render_template, request
from src.data_handle import handle_main

app = Flask(__name__, template_folder='templates', static_folder='web', static_url_path='/web')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, suppors_credentials=True, resources={r'/*'})  # 设置跨域
swagger = Swagger(app)


@app.route('/api/data/kg', methods=['POST'])
def get_data():
    # body = request.get_json()
    # formula_name, params = body['formulaName'], body['params']
    data = handle_main()
    return json.dumps(data, ensure_ascii=False)


@app.route('/api/data/cycle', methods=['POST'])
def get_cycle():
    # body = request.get_json()
    # name = body['name']
    data = {
        "result": [
            {
                "name": "袁天罡",
                "type": "人物"
            },
            {
                "name": "陆林轩",
                "type": "人物"
            },
            {
                "name": "李星云",
                "type": "人物"
            },
            {
                "name": "陆林轩",
                "type": "人物"
            }
            , {
                "name": "温韬",
                "type": "人物"
            },
            {
                "name": "李嗣源",
                "type": "人物"
            },
            {
                "name": "李克用",
                "type": "人物"
            },
            {
                "name": "女帝",
                "type": "人物"
            },
            {
                "name": "李茂贞",
                "type": "人物"
            },
            {
                "name": "李存勖",
                "type": "人物"
            },
            {
                "name": "龙泉剑",
                "type": "武器"
            }, {
                "name": "不良人",
                "type": "门派"
            }
        ]
    }
    return json.dumps(data, ensure_ascii=False)


@app.route('/index')
def getHtml():
    # global type_n_g, name_g
    # type_n_g = request.args.get("type")
    # name_g = request.args.get("name")
    return render_template('cycle.html')

@app.route('/kg')
def getkgHtml():
    # global type_n_g, name_g
    # type_n_g = request.args.get("type")
    # name_g = request.args.get("name")
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=Config.PYTHON_PORT)
