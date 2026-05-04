import uuid
from datetime import datetime, timedelta
from api.dependencies.database import SessionLocal
from api.models import model_loader
from api.models.user import User
from api.models.sandwiches import Sandwich
from api.models.resources import Resource
from api.models.product import Product
from api.models.deals import Deal
from api.models.recipes import Recipe
from api.models.orders import Order
from api.models.order_details import OrderDetail
from api.models.payments import Payment
from api.models.purchase_history import PurchaseHistory
from api.models.reviews import Review

model_loader.index()
db = SessionLocal()

try:
    # Users
    u1 = User(name="John Doe", email="john@example.com", phone_number="704-555-0101", address="123 Main St", is_recurring_customer=True)
    u2 = User(name="Jane Smith", email="jane@example.com", phone_number="704-555-0102", address="456 Oak Ave", is_recurring_customer=False)
    db.add_all([u1, u2])
    db.commit()
    db.refresh(u1); db.refresh(u2)
    print("Users seeded")

    # Sandwiches
    s1 = Sandwich(sandwich_name="BLT", price=8.99)
    s2 = Sandwich(sandwich_name="Club", price=10.99)
    s3 = Sandwich(sandwich_name="Veggie Delight", price=7.99)
    db.add_all([s1, s2, s3])
    db.commit()
    db.refresh(s1); db.refresh(s2); db.refresh(s3)
    print("Sandwiches seeded")

    # Resources (ingredients)
    r1 = Resource(item="Bread", amount=100)
    r2 = Resource(item="Bacon", amount=50)
    r3 = Resource(item="Lettuce", amount=80)
    r4 = Resource(item="Tomato", amount=60)
    r5 = Resource(item="Turkey", amount=40)
    db.add_all([r1, r2, r3, r4, r5])
    db.commit()
    db.refresh(r1); db.refresh(r2); db.refresh(r3); db.refresh(r4); db.refresh(r5)
    print("Resources seeded")

    # Products
    p1 = Product(name="BLT Sandwich", description="Classic BLT on sourdough", price=8.99, calories=450, food_category="Sandwiches")
    p2 = Product(name="Club Sandwich", description="Triple decker with turkey and bacon", price=10.99, calories=650, food_category="Sandwiches")
    p3 = Product(name="Veggie Wrap", description="Fresh vegetables in a flour wrap", price=7.99, calories=350, food_category="Wraps")
    p4 = Product(name="Chips", description="House-made potato chips", price=1.99, calories=150, food_category="Sides")
    db.add_all([p1, p2, p3, p4])
    db.commit()
    db.refresh(p1); db.refresh(p2); db.refresh(p3); db.refresh(p4)
    print("Products seeded")

    # Deals
    d1 = Deal(promo_code="SAVE10", description="10% off your order", deal_type="percent", discount_percent=10.00, expiration_date=datetime.now() + timedelta(days=30))
    d2 = Deal(promo_code="BOGO", description="Buy one sandwich get one free", deal_type="bogo", buy_quantity=1, get_quantity=1, expiration_date=datetime.now() + timedelta(days=30))
    db.add_all([d1, d2])
    db.commit()
    db.refresh(d1); db.refresh(d2)
    print("Deals seeded")

    # Recipes (sandwich ingredients)
    db.add_all([
        Recipe(sandwich_id=s1.id, resource_id=r1.id, amount=2),  # BLT: bread
        Recipe(sandwich_id=s1.id, resource_id=r2.id, amount=3),  # BLT: bacon
        Recipe(sandwich_id=s1.id, resource_id=r3.id, amount=1),  # BLT: lettuce
        Recipe(sandwich_id=s1.id, resource_id=r4.id, amount=1),  # BLT: tomato
        Recipe(sandwich_id=s2.id, resource_id=r1.id, amount=2),  # Club: bread
        Recipe(sandwich_id=s2.id, resource_id=r5.id, amount=2),  # Club: turkey
        Recipe(sandwich_id=s2.id, resource_id=r3.id, amount=1),  # Club: lettuce
        Recipe(sandwich_id=s2.id, resource_id=r4.id, amount=1),  # Club: tomato
        Recipe(sandwich_id=s3.id, resource_id=r1.id, amount=2),  # Veggie: bread
        Recipe(sandwich_id=s3.id, resource_id=r3.id, amount=2),  # Veggie: lettuce
        Recipe(sandwich_id=s3.id, resource_id=r4.id, amount=2),  # Veggie: tomato
    ])
    db.commit()
    print("Recipes seeded")

    # Orders
    o1 = Order(customer_name="Bob Guest", customer_phone="704-555-0199", customer_address="789 Pine Rd", order_type="delivery", order_status="delivered", tracking_number=str(uuid.uuid4()), total_price=10.98)
    o2 = Order(user_id=u1.id, order_type="takeout", order_status="ready", tracking_number=str(uuid.uuid4()), total_price=19.78, deal_id=d1.id)
    o3 = Order(user_id=u2.id, order_type="delivery", order_status="pending", tracking_number=str(uuid.uuid4()), total_price=8.99)
    db.add_all([o1, o2, o3])
    db.commit()
    db.refresh(o1); db.refresh(o2); db.refresh(o3)
    print("Orders seeded")

    # Order Details
    db.add_all([
        OrderDetail(order_id=o1.id, sandwich_id=s1.id, amount=1),
        OrderDetail(order_id=o2.id, sandwich_id=s2.id, amount=2),
        OrderDetail(order_id=o3.id, sandwich_id=s3.id, amount=1),
    ])
    db.commit()
    print("Order details seeded")

    # Payments
    pay1 = Payment(user_id=u1.id, order_id=o2.id, card_last_four="4242", card_brand="Visa", payment_type="credit", transaction_status="approved", transaction_reference=str(uuid.uuid4()), amount=19.78)
    pay2 = Payment(user_id=u2.id, order_id=o3.id, card_last_four="1234", card_brand="Mastercard", payment_type="credit", transaction_status="approved", transaction_reference=str(uuid.uuid4()), amount=8.99)
    db.add_all([pay1, pay2])
    db.commit()
    db.refresh(pay1); db.refresh(pay2)
    print("Payments seeded")

    # Purchase History
    db.add_all([
        PurchaseHistory(user_id=u1.id, order_id=o2.id, product_id=p2.id, deal_id=d1.id, quantity=2, unit_price=10.99, total_price=19.78),
        PurchaseHistory(user_id=u2.id, order_id=o3.id, product_id=p1.id, quantity=1, unit_price=8.99, total_price=8.99),
    ])
    db.commit()
    print("Purchase history seeded")

    # Reviews
    db.add_all([
        Review(user_id=u1.id, product_id=p1.id, score=5, review_text="Amazing BLT, super fresh ingredients!"),
        Review(user_id=u2.id, product_id=p2.id, score=4, review_text="Club sandwich was great, a little pricey though."),
        Review(user_id=u1.id, product_id=p3.id, score=3, review_text="Veggie wrap was okay, could use more flavor."),
    ])
    db.commit()
    print("Reviews seeded")

    print("\nAll done! Database seeded successfully.")

except Exception as e:
    db.rollback()
    print(f"Error: {e}")
finally:
    db.close()
