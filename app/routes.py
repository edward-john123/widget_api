import logging
from typing import List

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from .extensions import db
from .models import Widget
from .schemas import WidgetSchema

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

