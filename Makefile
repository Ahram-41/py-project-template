.PHONY: format lint clean install

# Install dependencies with uv
install:
	uv sync --extra dev

# Format code
format:
	black ./src
	isort ./src

# Check formatting
lint:
	black --check src/
	isort --check-only src/

# Clean up
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.egg-info" -type d -exec rm -rf {} + 