FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements (even if minimal)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command: run a single experiment
CMD ["bash", "scripts/run_experiment.sh"]
