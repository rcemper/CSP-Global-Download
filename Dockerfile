ARG IMAGE=intersystemsdc/iris-community
FROM $IMAGE

USER root

WORKDIR /opt/irisapp
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisapp

####  fix interactive input issues
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

##### Install Python
RUN \
  apt-get update && \
  apt-get -y install python3 python3-pip

USER ${ISC_PACKAGE_MGRUSER}

COPY src src
COPY module.xml module.xml
COPY iris.script iris.script

RUN iris start IRIS \
	&& iris session IRIS < iris.script \
    && iris stop IRIS quietly 