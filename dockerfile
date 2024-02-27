# Use an existing Docker image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .


# Install any dependencies
RUN pip install -r requirements.txt --default-timeout=100 future

# Copy the rest of the application code to the working directory
COPY . .

# Set the API key environment variable
# ENV OPENAI_API_KEY=${API_KEY}

EXPOSE 8501

# Command to run your application

CMD ["streamlit","run","app.py"]
