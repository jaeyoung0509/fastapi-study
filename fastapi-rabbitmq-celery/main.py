from fastapi import FastAPI 
from celery_worker import create_order
from model import Order

#Create Fastapi App
app = FastAPI()

#Create order endpoint
@app.post('/order')
def add_order(order : Order):
    create_order.delay(order.customer_name , order.order_quantity)
    #use delay() method to call the celery task
    return {"message" : "Order received"}