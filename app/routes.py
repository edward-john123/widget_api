import logging
from typing import List

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from .extensions import db
from .models import Widget
from .schemas import WidgetSchema, WidgetUpdateSchema

blp = Blueprint(
    "widgets", __name__, url_prefix="/widgets", description="Operations on widgets"
)
logger = logging.getLogger(__name__)


@blp.route("/")
class WidgetList(MethodView):
    @blp.response(200, WidgetSchema(many=True))
    def get(self) -> List[Widget]:
        """List all widgets"""
        # TODO: Add pagination
        return Widget.query.all()

    @blp.arguments(WidgetSchema)
    @blp.response(201, WidgetSchema)
    def post(self, new_data) -> Widget:
        """Create a new widget"""
        widget = Widget(**new_data)
        try:
            db.session.add(widget)
            db.session.commit()
            logger.info(f"Widget with ID {widget.id} Created")
        except SQLAlchemyError as e:
            logger.error(f"DB Error occurred: {e}")
            db.session.rollback()
            abort(500, message=str(e))
        return widget


@blp.route("/<int:widget_id>")
class WidgetById(MethodView):
    def _get_widget(self, widget_id: int) -> Widget:
        widget = Widget.query.get(widget_id)
        if not widget:
            logger.error(f"Widget with ID {widget_id} not found")
            abort(404, message="Widget not found.")
        return widget

    @blp.response(200, WidgetSchema)
    def get(self, widget_id: int) -> Widget:
        """Get a widget by ID"""
        widget = self._get_widget(widget_id)
        return widget

    @blp.arguments(WidgetUpdateSchema)
    @blp.response(200, WidgetSchema)
    def put(self, update_data, widget_id: int) -> Widget:
        """Update an existing widget"""
        widget = self._get_widget(widget_id)

        if "name" in update_data:
            widget.name = update_data["name"]
        if "num_parts" in update_data:
            widget.num_parts = update_data["num_parts"]
        try:
            db.session.add(widget)
            db.session.commit()
            logger.info(f"Widget with ID {widget.id} Updated")
        except SQLAlchemyError as e:
            logger.error(f"DB Error occurred: {e}")
            db.session.rollback()
            abort(500, message=str(e))
        return widget

    @blp.response(204)
    def delete(self, widget_id: int):
        """Delete a widget"""
        widget = self._get_widget(widget_id)
        try:
            db.session.delete(widget)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"DB Error occurred: {e}")
            db.session.rollback()
            abort(500, message=str(e))
        return ""
