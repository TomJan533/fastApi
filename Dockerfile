FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (gcc for compiling, libmariadb-dev for MySQL development headers)
RUN apt-get update && apt-get install -y gcc libmariadb-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
