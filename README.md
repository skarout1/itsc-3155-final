# Online Restaurant Ordering System
ITSC-3155 Software Engineering — Group Project Part 3

A REST API for an online restaurant ordering system built with Python FastAPI, SQLAlchemy ORM, and MySQL. The API supports both customer and restaurant staff workflows, addressing 14 core business requirements across ordering, payments, reviews, inventory, and promotions.

## Demo Video
[Watch on YouTube](https://www.youtube.com/watch?v=6hm6SxeAiBU)

### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
