FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY tests ./tests
COPY examples ./examples
COPY scripts ./scripts

CMD ["python", "scripts/run_demo.py"]
