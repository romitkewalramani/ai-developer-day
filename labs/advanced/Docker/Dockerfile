# Multi-language development container for workshop (Express.js + FastAPI)
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    build-essential \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20.x (for TypeScript/Nest.js)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g typescript ts-node nodemon @types/node

# Install Python 3.11+ with pip and common tools
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3-pip \
    python3.11-venv \
    && rm -rf /var/lib/apt/lists/*

# Install Python file watcher and FastAPI dependencies
RUN pip3 install watchdog uvicorn[standard] fastapi

# Set up working directory
WORKDIR /workspace

# Configure Git (workshop participants can override)
# The workspace will be mounted from the host labs/advanced directory
RUN git config --global --add safe.directory /workspace
RUN git config --global --add safe.directory '*'

# Expose development ports
EXPOSE 3000 8000

# Default command - keeps container running
CMD ["tail", "-f", "/dev/null"]