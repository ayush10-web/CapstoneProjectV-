# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app will run (if needed)
EXPOSE 8080

# Define the command to run the app
CMD ["python", "-m", "streamlit", "run", "app.py"]