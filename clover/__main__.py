import uvicorn
from clover import IS_DEV

u_ar: dict = {"log_level": "info", "port": 8000, "reload_dirs": []}

if IS_DEV:
    u_ar["reload"] = True
    u_ar["reload_dirs"] = ["./clover"]

uvicorn.run("clover:app", **u_ar)
