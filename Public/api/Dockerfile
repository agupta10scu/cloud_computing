#Based on Python
FROM python

# Install the python library flask
RUN pip install Flask

# Create a Volume called app
VOLUME app

# Set this is the working directory
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["api.py"]