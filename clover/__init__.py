__version__ = "0.1.0"
IS_DEV = True
from dotenv import load_dotenv

load_dotenv(".env")

from clover.books.routes import router as book_router
from clover.app import app
