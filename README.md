# py-project-template

A modern Python project template using `uv` for fast dependency management and packaging.

## Features

- 🚀 **Fast dependency management** with [uv](https://github.com/astral-sh/uv)
- 🛠️ **Development tools** pre-configured:
  - [Black](https://black.readthedocs.io/) for code formatting
  - [isort](https://pycqa.github.io/isort/) for import sorting
  - [pytest](https://docs.pytest.org/) for testing
- 📦 **Modern Python packaging** with `pyproject.toml`
- 🧹 **Comprehensive `.gitignore`** for Python projects
- ⚡ **Makefile** for common development tasks
- 📁 **Source-based project structure** (`src/` layout)

## Quick Start

1. **Clone this template**:
   ```bash
   git clone <your-repo-url>
   cd py-project-template
   ```

2. **Set up the environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync --extra dev
   ```

3. **Customize for your project**:
   - Update `pyproject.toml` with your project details
   - Add your source code to the `src/` directory
   - Update this README

## Development Workflow

### Available Make Commands

```bash
make install    # Install dependencies with development extras
make format     # Format code with black and isort
make lint       # Check code formatting
make clean      # Clean up generated files
```

**Configuration**


- **Black**: 88 character line length
- **isort**: Black-compatible profile
- **Python**: Requires Python >=3.12
- **Testing**: pytest framework included

## Customization

1. **Update project metadata** in `pyproject.toml`:
   ```toml
   name = "your-project-name"
   version = "0.1.0"
   description = "Your project description"
   authors = [{name = "Your Name", email = "your.email@example.com"}]
   ```

2. **Add dependencies** via `uv add <dependency>`


3. **Add source code** to the `src/` directory

## Requirements

- Python >=3.12
- [uv](https://github.com/astral-sh/uv) package manager