import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('7413746495:AAEmHt1PgoNqg3Ly6hntSjYGvHIgx3RIHHE')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
