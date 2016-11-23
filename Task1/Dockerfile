FROM centos:centos6

MAINTAINER Nikhil Reddy <nikhilreddy.araga@gmail.com>

# Install yum dependencies
RUN yum -y update && \
    yum groupinstall -y development && \
    yum install -y \
    bzip2-devel \
    git \
    hostname \
    openssl \
    openssl-devel \
    sqlite-devel \
    sudo \
    tar \
    wget \
    zlib-dev

# Install python2.7
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz && \
    tar xvfz Python-2.7.8.tgz && \
    rm Python-2.7.8.tgz && \
    cd Python-2.7.8 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall

# Install setuptools + pip
RUN cd /tmp && \
    wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz && \
    tar -xvf setuptools-1.4.2.tar.gz && \
    rm setuptools-1.4.2.tar.gz && \
    cd setuptools-1.4.2 && \
    python2.7 setup.py install && \
    curl https://bootstrap.pypa.io/get-pip.py | python2.7 - && \
    pip install virtualenv

# Install MongoDB
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install mongodb-server && \
    mkdir -p /data/db

EXPOSE 27017

# Install Oracle Java 8
RUN wget --no-cookies \
         --no-check-certificate \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
         "http://download.oracle.com/otn-pub/java/jdk/8u31-b13/jre-8u31-linux-x64.rpm" \
         -O /tmp/jre-8u31-linux-x64.rpm
RUN chmod 755 /tmp/jre-8u31-linux-x64.rpm && \
    rpm -ivh /tmp/jre-8u31-linux-x64.rpm && \
    rm /tmp/jre-8u31-linux-x64.rpm

ENV JAVA_HOME /usr/java/default

# Install Tomcat 7
RUN wget "http://apache.mirrors.spacedump.net/tomcat/tomcat-7/v7.0.73/bin/apache-tomcat-7.0.73.tar.gz" \
		 -O /apache-tomcat-7.0.73.tar.gz && \
	  tar xvzf /apache-tomcat-7.0.73.tar.gz && \
    rm /apache-tomcat-7.0.73.tar.gz && \
    rm -rf /apache-tomcat-7.0.73/webapps/docs && \
    rm -rf /apache-tomcat-7.0.73/webapps/examples && \
    mv /apache-tomcat-7.0.73/ /usr/local/

RUN yum -y install tomcat-native && \
    yum clean all

# Expose the standard Tomcat ports
EXPOSE 8080
