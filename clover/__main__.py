import uvicorn
from clover import app

uvicorn.run("clover:app", log_level="info", reload=True, reload_dirs=["./clover"])
