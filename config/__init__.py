class Config:
    PYTHON_PORT = "6950"
    GRAPH_HOST = "http://localhost:7474/"
    GRAPH_USER = "neo4j"
    GRAPH_PASSWD = "123456"



import os

# 读取环境变量,更新到Config后，以和容器一起使用
for k in os.environ:
    if k in Config.__dict__:
        #        logger.info(f'use environ var:{k},{os.environ.get(k)}')
        setattr(Config, k, os.environ.get(k))
CONFIG = Config()
for k in os.environ:
    if k in CONFIG.__dict__:
        #        logger.info(f'use environ var:{k},{os.environ.get(k)}')
        CONFIG.__dict__[k] = os.environ.get(k)
