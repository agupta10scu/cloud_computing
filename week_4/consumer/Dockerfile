FROM python

# Install the python library flask
# COPY requirements.txt requirements.txt
RUN pip install requests
RUN pip install flask
RUN pip install jsonify


# Make this a Volume
VOLUME app

# Make sure this is the working directory
WORKDIR /app

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["consumer.py"]