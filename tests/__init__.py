from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from main import app




client = TestClient(app, base_url="http://test/api/v1")
