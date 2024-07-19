# Use an official Python runtime as a parent image
FROM python:3.13.0a1-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set destination for COPY
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run
CMD [ "gunicorn", "--bind=0.0.0.0:8000", "wsgi:app" ]