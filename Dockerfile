# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set the working directory
WORKDIR /app

# Copy necessary files into the container
COPY . .

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run your main script when the container starts
CMD ["python3", "main.py"]
