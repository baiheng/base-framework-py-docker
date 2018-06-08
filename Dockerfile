From daocloud.io/centos:7

RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
		&& curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo \
		&& yum clean all \
		&& yum makecache \
		&& yum install -y epel-release \
		&& yum install -y gcc gcc-c++ zlib zlib-devel openssl openssl-devel \
		&& yum install -y python36 python-setuptools python-devel mysql MySQL-python redis \
		&& yum install -y wget \
		&& wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate -O /tmp/get-pip.py\
		&& python3.6 /tmp/get-pip.py

COPY ./requirement.txt /tmp

RUN yum install -y python36-devel.x86_64 \
	&&	pip3 install -r /tmp/requirement.txt 

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \
	&& echo "Asia/Shanghai" > /etc/timezone 

WORKDIR /work
ENV SETTINGS PRODUCTION 
CMD /bin/bash ./bin/run-docker.sh
