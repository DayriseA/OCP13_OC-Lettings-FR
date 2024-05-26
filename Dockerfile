FROM python:3.11-slim as builder

# Install curl to get poetry
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# Add Poetry to PATH
ENV PATH="/etc/poetry/bin:$PATH"

# Set Poetry configuration
RUN poetry config virtualenvs.in-project true

# Copy only needed files
COPY pyproject.toml poetry.lock /app/

WORKDIR /app

# Install main dependencies
RUN poetry install --no-dev --no-interaction


# Runtime / Final image
FROM python:3.11-slim

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

WORKDIR /app

# Copy the rest of the files
COPY . /app

# Create a directory for static files
RUN mkdir /app/staticfiles

# Set the PATH to the venv
ENV PATH="/app/.venv/bin:$PATH"

# Fix line endings for Unix compatibility (Windows uses CRLF, Unix uses LF)
RUN sed -i 's/\r$//g' /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Create a user and group to run the application
RUN addgroup --system app && adduser --system --group app
RUN chown -R app:app /app

EXPOSE 8080

USER app

# Not intended to run alone so we will start the server in docker-compose file
ENTRYPOINT [ "/app/entrypoint.sh" ]