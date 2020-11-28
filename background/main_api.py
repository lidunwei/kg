# -*- coding: utf-8 -*-
import json
from flask import Flask, request, jsonify, url_for
from flasgger import Swagger
from flask_cors import *
from background.config import Config
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, suppors_credentials=True, resources={r'/*'})  # 设置跨域
swagger = Swagger(app)


@app.route('/api/data/', methods=['POST'])
def get_data():
    try:
        body = request.get_json()
        formula_name, params = body['formulaName'], body['params']

    except Exception as e:
        print(e)
        return json.dumps({'resultMsg': '异常,请联系开发者', 'result_code': 1}, ensure_ascii=False)


if __name__ == '__main__':
    app.run('0.0.0.0', port=Config.PYTHON_PORT)
