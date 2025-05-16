from app.models import Widget
from tests.factories import WidgetFactory


def test_create_widget(client, init_db):
    """Test widget creation."""
    response = client.post("/widgets/", json={"name": "Test Widget 1", "num_parts": 10})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Test Widget 1"
    assert data["num_parts"] == 10
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

    # Check database
    with client.application.app_context():
        widget = Widget.query.get(data["id"])
        assert widget is not None
        assert widget.name == "Test Widget 1"


def test_create_widget_invalid_data(client, init_db):
    """Test widget creation with invalid data (e.g., missing name)."""
    response = client.post("/widgets/", json={"num_parts": 5})
    assert response.status_code == 422
    data = response.get_json()
    assert "errors" in data
    assert "name" in data["errors"]["json"]

    response = client.post("/widgets/", json={"name": "N" * 65, "num_parts": 1})
    assert response.status_code == 422
    data = response.get_json()
    assert "name" in data["errors"]["json"]


def test_list_widgets(client, init_db):
    """Test listing all widgets."""
    widgets = WidgetFactory.create_batch(5)
    response = client.get("/widgets/")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == len(widgets)
    assert data[0]["name"] == widgets[0].name
    assert data[1]["name"] == widgets[1].name


def test_list_widgets_empty(client, init_db):
    """Test listing widgets when there are none."""
    response = client.get("/widgets/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

