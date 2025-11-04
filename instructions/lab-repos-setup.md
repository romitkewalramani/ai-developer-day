# Development Environment Setup Guide

This guide will help you set up your development environment for the AI Upskills Workshop. You can choose between using Dev Containers (recommended) or setting up dependencies manually on your local machine.

## Prerequisites

- **Cursor IDE** installed and running
- For Dev Containers option: **Docker Desktop** installed and running

---

## Option 1: Dev Containers Setup (Recommended)

This option uses Docker containers to provide a consistent development environment with all dependencies pre-configured. This is the recommended approach as it ensures everyone has the same setup.

### Step 1: Verify Docker Desktop

1. Ensure **Docker Desktop** is installed and running on your machine
2. Verify Docker is running by checking the Docker Desktop application icon in your system tray/menu bar

### Step 2: Open the Project in Cursor

1. Open Cursor IDE
2. Open the project folder: `ai-developer-day`
3. Navigate to the `labs/advanced` directory

### Step 3: Reopen in Dev Container

1. Press `F1` (or `Cmd+Shift+P` on Mac / `Ctrl+Shift+P` on Windows/Linux) to open the command palette
2. Type: `Dev Containers: Reopen in Container`
3. Select the option from the dropdown
4. Wait for Cursor to build and start the container (this may take a few minutes the first time)

### Step 4: Verify the Setup

Once the container is running:

1. The container includes:
   - **Node.js 20.x** with TypeScript, ts-node, and nodemon
   - **Python 3.11** with pip and virtual environment support
   - **FastAPI** and **NestJS** dependencies pre-installed
   - All necessary development tools and extensions

2. The following ports are automatically forwarded:
   - **Port 3000**: TypeScript/NestJS applications
   - **Port 8000**: Python/FastAPI applications

### Step 5: Navigate to Your Project

Once inside the container, navigate into your chosen project:

- **For TypeScript**: `cd Typescript`
- **For Python**: `cd Python`

You can now follow the project-specific setup instructions in the respective README.md files if needed.

### Troubleshooting Dev Containers

- **Container won't start**: Ensure Docker Desktop is running and has sufficient resources allocated
- **Port conflicts**: If ports 3000 or 8000 are already in use, you may need to stop other services or modify the port mappings
- **Slow first build**: The initial container build downloads images and installs dependencies, which can take 5-10 minutes. Subsequent starts will be faster

---

## Option 2: Manual Setup (Local Installation)

If you prefer not to use Dev Containers, you can install dependencies directly on your local machine. Choose either the TypeScript or Python project based on your preference.

### TypeScript Project Setup

1. Navigate to the TypeScript project directory:

   ```bash
   cd labs/advanced/workspace/Typescript
   ```

2. Follow the setup instructions in the **README.md** file:

3. Typically, the setup involves:
   - Installing Node.js (v20 or higher recommended)
   - Running `npm install` to install dependencies
   - Running `npm run start:dev` to start the development server

### Python Project Setup

1. Navigate to the Python project directory:
   ```bash
   cd labs/advanced/workspace/Python
   ```

2. Follow the setup instructions in the **README.md** file:

3. Typically, the setup involves:
   - Installing Python 3.11 or higher
   - Creating a virtual environment (recommended)
   - Installing dependencies with `pip install -r requirements.txt`
   - Running the server with `uvicorn main:app --reload`

---

## Next Steps

After completing either setup option:

1. **Verify your setup** by running the development server for your chosen project
2. **Test the API** by accessing:
   - TypeScript: `http://localhost:3000/api` (Swagger UI)
   - Python: `http://localhost:8000/docs` (Swagger UI)
3. **Review the project README** for API endpoints and usage examples

---

## Need Help?

If you encounter any issues during setup:

1. Check the project-specific README.md files for detailed instructions
2. Verify all prerequisites are installed and running
3. Ensure ports 3000 (TypeScript) and 8000 (Python) are not already in use by other applications

---

## Summary

- **Dev Containers** (Option 1): Provides a consistent, isolated environment with all dependencies pre-configured
- **Manual Setup** (Option 2): Gives you more control but requires installing and managing dependencies yourself

Choose the option that best fits your workflow and experience level!

