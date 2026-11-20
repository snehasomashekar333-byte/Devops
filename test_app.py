from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Delivery Metrics Exporter is running!" in response.data

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200

def test_metrics():
    response = app.test_client().get("/metrics")
    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "delivery-metrics-exporter"
    assert "requests_total" in data
    assert "uptime_seconds" in data
