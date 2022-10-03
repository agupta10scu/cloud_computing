#python latest version as of 9/29/2022
FROM python:3.10.7
USER root

#RUN pip3 install jupyter  {to install jupyter notebook}
#jupyter notebook          {launch jupyter notebook}


#creating user
ENV JUPYTER_USER anjidocker
RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8888

WORKDIR /home/${JUPYTER_USER}
RUN mkdir jupyter_notebooks
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt
RUN wget -P jupyter_notebooks https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb

RUN chown -R ${JUPYTER_USER}:${JUPYTER_USER} jupyter_notebooks

RUN chmod 755 jupyter_notebooks/Introduction.ipynb

USER $(JUPYTER_USER)
WORKDIR /home/$(JUPYTER_USER)/jupyter_notebooks

#launching the jupyter server
CMD jupyter notebook --ip=0.0.0.0 --port 8888


