import requests
import os
import json

BACK_END_URL = os.getenv('BACK_END_URL')

async def get_client():
    
    clients = requests.get(f'{BACK_END_URL}/api/v1/clients')
    
    clients_list = clients.json()

    return clients_list.get("clients")

async def get_products():
    products = requests.get(f'{BACK_END_URL}/api/v1/products')
    
    products_list = products.json()

    return products_list.get("products")
