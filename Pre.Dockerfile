FROM centos7-python3
COPY requirements.txt . 
RUN yum install -y git && /root/miniconda3/bin/pip install --trusted-host mirrors.aliyun.com  -i http://mirrors.aliyun.com/pypi/simple/  -r requirements.txt
