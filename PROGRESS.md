# Project Progress

## Completed

### Orders (`api/models/orders.py`, `api/schemas/orders.py`, `api/controllers/orders.py`, `api/routers/orders.py`)
Full CRUD plus two special endpoints:
- `GET /orders/track/{tracking_number}` — customer order tracking by tracking number
- `GET /orders/filter?start_date=&end_date=` — filter orders by date range for staff

Order model was updated to support:
- Guest ordering (`customer_name`, `customer_phone`, `customer_address`) — `user_id` made nullable
- Order type (`takeout` or `delivery`)
- Order status (`pending`, `preparing`, `ready`, `delivered`)
- Auto-generated UUID tracking number on creation
- Optional promo code linkage via `deal_id` FK

### Order Details (`api/controllers/order_details.py`, `api/routers/order_details.py`)
Full CRUD.

### Resources (`api/controllers/resources.py`, `api/routers/resources.py`)
Full CRUD plus one special endpoint:
- `GET /resources/check/{sandwich_id}` — checks if enough ingredients exist to fulfill an order, returns which resources are insufficient

---

## In Progress (assigned to group members, due Wednesday)

| Tables | Endpoints needed |
|---|---|
| `products`, `reviews` | Full CRUD + `GET /products/search?category=` |
| `deals`, `purchase_history` | Full CRUD |
| `sandwiches`, `recipes` | Full CRUD |

---

## Still Needed (after group submits)

- Wire all new routers into `api/routers/index.py`
- Add all new routers to `api/models/model_loader.py`
- Full CRUD for `users` and `payments`
- `GET /payments/revenue?date=` — total revenue on a given day
- Populate database with sample data for demo
- At least one additional pytest unit test passing
- Sprint Backlog document (Sprint 1 + Sprint 2)
- Sprint Review document (Sprint 1 + Sprint 2)
- 4–5 min recorded video demo uploaded to GitHub

---

## Evaluation Checklist

### Restaurant Staff (7 questions, 10.5 pts)
| Question | Endpoint | Status |
|---|---|---|
| Create/update/delete menu items | `POST/PUT/DELETE /products` | Pending (Person 2) |
| Alert if insufficient ingredients | `GET /resources/check/{sandwich_id}` | Done |
| View all orders / specific order | `GET /orders`, `GET /orders/{id}` | Done |
| Identify low-rated dishes / complaints | `GET /reviews` + `GET /products/{id}` | Pending (Person 2) |
| Create/manage promo codes | `POST/PUT/DELETE /deals` | Pending (Person 3) |
| Total revenue on a given day | `GET /payments/revenue?date=` | Not started |
| Orders within a date range | `GET /orders/filter?start_date=&end_date=` | Done |

### Customer (7 questions, 10.5 pts)
| Question | Endpoint | Status |
|---|---|---|
| Place order as guest | `POST /orders` (no user_id required) | Done |
| Pay for an order | `POST /payments` | Not started |
| Takeout vs. delivery preference | `POST /orders` with `order_type` field | Done |
| Track order by tracking number | `GET /orders/track/{tracking_number}` | Done |
| Search food by category | `GET /products/search?category=` | Pending (Person 2) |
| Rate and review dishes | `POST /reviews` | Pending (Person 2) |
| Apply promo code to order | `POST /orders` with `deal_id` field | Done |
