FROM kg:pre
WORKDIR /usr/local/app
COPY .  /usr/local/app
COPY requirements.txt .
RUN yum install -y git && /root/miniconda3/bin/pip install --trusted-host mirrors.aliyun.com  -i http://mirrors.aliyun.com/pypi/simple/  -r requirements.txt
EXPOSE 6012
ENTRYPOINT ["/root/miniconda3/bin/python"]
CMD ["-u","main_api.py"]
