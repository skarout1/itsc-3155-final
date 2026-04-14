from . import orders, order_details, recipes, sandwiches, resources, user, purchase_history, product, deals

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    purchase_history.Base.metadata.create_all(engine)
    user.Base.metadata.create_all(engine)
    product.Base.metadata.create_all(engine)
    deals.Base.metadata.create_all(engine)