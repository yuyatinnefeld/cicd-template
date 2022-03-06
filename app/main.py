from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.skills import language, cloud, devops


description = """Resume Backend Service API 🚀"""

app = FastAPI(
    title="Resume Backend API",
    description=description,
    version="0.0.1",
    contact={
        "name": "Yuya Tinnefeld",
        "url": "https://yuyatinnefeld-resume-xljcoys6wa-ew.a.run.app",
        "email": "yuyatinnefeld@gmail.com",
    },
    license_info={
        "name": "Visit Github",
        "url": "https://github.com/yuyatinnefeld",
    },
    
)


@app.get("/")
def read_root():
    item = {"msg": "FastAPI World"}
    return JSONResponse(content=item)

@app.get("/language")
async def read_language():
    return JSONResponse(content=language)

@app.get("/cloud")
async def read_cloud():
    return JSONResponse(content=cloud)

@app.get("/devops")
async def read_devops():
    return JSONResponse(content=devops)
