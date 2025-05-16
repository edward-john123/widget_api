import factory

from app.models import Widget


class WidgetFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Widget
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
    num_parts = factory.Faker("pyint", min_value=1, max_value=1000)
