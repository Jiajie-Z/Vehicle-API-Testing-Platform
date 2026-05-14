# Vehicle API Testing Platform

A vehicle connectivity API testing project built around a simulated connected-car backend service.

The project includes API development, automated API regression tests, JSON Schema response validation, performance testing with Locust, Docker-based deployment, and GitHub Actions CI.

## Features

- Simulated connected vehicle APIs for authentication, vehicle status, trip records, alerts, and telemetry upload
- Automated API tests using PyTest
- JSON Schema validation for API response structure
- Performance testing scenarios using Locust
- Docker Compose support for local deployment
- GitHub Actions workflow for automated regression testing

## Tech Stack

- Python
- FastAPI
- PyTest
- JSON Schema
- Locust
- Docker
- GitHub Actions

## API Overview

| Module | Endpoint | Description |
| --- | --- | --- |
| Auth | `POST /api/auth/login` | User login |
| Vehicles | `GET /api/vehicles` | Get vehicle list |
| Vehicles | `GET /api/vehicles/{vehicle_id}/status` | Get vehicle status |
| Vehicles | `GET /api/vehicles/{vehicle_id}/trips` | Get vehicle trip records |
| Alerts | `POST /api/alerts` | Submit vehicle alert |
| Alerts | `GET /api/alerts` | Get alert list |
| Telemetry | `POST /api/telemetry` | Upload vehicle telemetry data |

## Project Structure

```text
vehicle-api-testing-platform/
  app/
    main.py
    models.py
    data_store.py
    auth.py
    routes/
  api_tests/
    clients/
    schemas/
    tests/
    conftest.py
  performance_tests/
    locustfile.py
  docs/
    test-plan.md
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

## Quick Start

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API service:

```bash
uvicorn app.main:app --reload --port 9000
```

Health check:

```text
http://127.0.0.1:9000/health
```

Swagger API documentation:

```text
http://127.0.0.1:9000/docs
```

## Test Account

```text
username: test_driver
password: Drive@123
```

## Run API Tests

```bash
pytest api_tests -v
```

Current automated test result:

```text
14 passed
```

The API test suite covers:

- Successful login and invalid password scenarios
- Missing or invalid authentication token
- Vehicle list query
- Online and offline vehicle status query
- Unknown vehicle error handling
- Trip record query
- Alert creation and invalid alert type validation
- Telemetry upload and boundary validation for battery level and location

## Run Performance Tests

Start the API service first:

```bash
uvicorn app.main:app --reload --port 9000
```

Start Locust:

```bash
locust -f performance_tests/locustfile.py --host http://127.0.0.1:9000
```

Open the Locust web UI:

```text
http://localhost:8089
```

Example performance test result:

```text
Total requests: 2166
Failures: 0
Failure rate: 0%
RPS: 8.3
Average response time: 2.3 ms
P95 response time: 3 ms
P99 response time: 8 ms
Max response time: 52 ms
```

## Docker

Build and start the service:

```bash
docker compose up --build
```

Visit:

```text
http://127.0.0.1:9000/health
```

Stop the service:

```bash
docker compose down
```

## Test Plan

The test plan includes test scope, test design methods, API coverage, and performance testing strategy.

See:

```text
docs/test-plan.md
```

## Notes

This project is designed as a practical testing portfolio project for API test automation, test framework design, and connected-vehicle service validation.
