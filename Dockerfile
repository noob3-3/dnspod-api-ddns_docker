FROM python:3.8-alpine
ENV TZ=Asia/Shanghai
RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt -i https://pypi.douban.com/simple
WORKDIR /code
CMD ["python", "/code/ddns_dns_pod.py"]