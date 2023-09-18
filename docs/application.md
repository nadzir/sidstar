## Application
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

Backend server is developed using FastAPI

### Quick Start

```bash
## Install dev dependencies
pip install -r requirements-dev.txt

## Install dependencies
pip install -r requirements.txt

## Start server
python main.py

## Health Check
curl localhost:8000/health
```

### URLS

API Documentation
- http://thales.ethsock.com/docs
- http://thales.ethsock.com/redocs

Deliverables
- http://thales.ethsock.com/api/waypoint/WSSS/sid/top
- http://thales.ethsock.com/api/waypoint/WSSS/star/top

### Folder Structure

```
├── api     - API Router
├── app     - Application Core Logic
├── lib     - Supporting library and common utilities
├── main.py - Entry point
```

### Running Test

Test are name using `method_should_when` convention

Command to run the test
```
pytest -v
```