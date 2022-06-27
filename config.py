from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['USER']
password = os.environ['PASSWORD']
host = os.environ['HOST']
database = os.environ['DATABASE']
port = os.environ['PORT']

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
print(DATABASE_CONNECTION_URI)