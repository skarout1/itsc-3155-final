from . import orders, order_details, deals, product, purchase_history, recipes, resources, reviews, sandwiches, users, payments


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(deals.router)
    app.include_router(product.router)
    app.include_router(purchase_history.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(reviews.router)
    app.include_router(sandwiches.router)
    app.include_router(users.router)
    app.include_router(payments.router)
