from fastapi import FastAPI
from api.users import router
import uvicorn

app: FastAPI =  FastAPI()

app.include_router(router=router)
@app.get("/")
async def root():
    return {"message": "User Profile"}
if(__name__ == '__main__'):
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)