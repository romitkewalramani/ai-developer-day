# Disney Movies API

## Installation

1. **Create a virtual environment** (recommended for non-devcontainer):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload during development.

The API will be available at:

- **API Base URL**: `http://localhost:8000`
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`
