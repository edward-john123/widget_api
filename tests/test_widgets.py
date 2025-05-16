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


def test_get_widget(client, init_db):
    """Test retrieving a single widget."""
    widget = WidgetFactory()
    response = client.get(f"/widgets/{widget.id}")
    assert response.status_code == 200

    data = response.get_json()
    assert data["name"] == widget.name
    assert data["num_parts"] == widget.num_parts


def test_get_nonexistent_widget(client, init_db):
    """Test retrieving a widget that does not exist."""
    response = client.get("/widgets/-999")
    assert response.status_code == 404


def test_update_widget(client, init_db, db):
    """Test updating an existing widget."""
    widget = WidgetFactory()
    update_payload = {"name": "New Widget Name", "num_parts": 20}
    response = client.put(f"/widgets/{widget.id}", json=update_payload)
    assert response.status_code == 200

    assert response.is_json, f"Response was not JSON: {response.data}"
    assert response.json["name"] == update_payload["name"]
    assert response.json["num_parts"] == update_payload["num_parts"]
    assert response.json["id"] == widget.id
    assert response.json["updated_at"] != widget.updated_at

    with client.application.app_context():
        widget = Widget.query.get(widget.id)
        assert widget.name == update_payload["name"]
        assert widget.num_parts == 20


def test_update_widget_partial(client, init_db):
    """Test partially updating an existing widget."""
    widget = WidgetFactory()
    update_payload = {"name": "New Name Only"}
    response = client.put(f"/widgets/{widget.id}", json=update_payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "New Name Only"
    assert data["num_parts"] == widget.num_parts


def test_update_nonexistent_widget(client, init_db):
    """Test updating a widget that does not exist."""
    response = client.put("/widgets/-999", json={"name": "Ghost Widget"})
    assert response.status_code == 404


def test_delete_widget(client, init_db):
    """Test deleting a widget."""
    widget = WidgetFactory()
    delete_response = client.delete(f"/widgets/{widget.id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/widgets/{widget.id}")
    assert get_response.status_code == 404

    with client.application.app_context():
        widget = Widget.query.get(widget.id)
        assert widget is None


def test_delete_nonexistent_widget(client, init_db):
    """Test deleting a widget that does not exist."""
    response = client.delete("/widgets/-999")
    assert response.status_code == 404
