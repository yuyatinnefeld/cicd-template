"""FastAPI Backend """
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.skills import language, cloud, devops


app = FastAPI(
    title="Resume Backend API",
    description="Resume Backend Service API 🚀",
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
    """Home Endpoint"""
    item = {"msg": "FastAPI World"}
    return JSONResponse(content=item)


@app.get("/language")
async def read_language():
    """Language Endpoint"""
    return JSONResponse(content=language)


@app.get("/cloud")
async def read_cloud():
    """Cloud Endpoint"""
    return JSONResponse(content=cloud)


@app.get("/devops")
async def read_devops():
    """DevOps Endpoint"""
    return JSONResponse(content=devops)
