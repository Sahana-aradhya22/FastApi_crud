from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import create_item, get_item, update_item, delete_item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"} 

@app.post("/items/")
async def create_item_endpoint(name: str, description: str, db: AsyncSession = Depends(get_db)):
    return await create_item(db, name, description)

@app.get("/items/{item_id}")
async def read_item_endpoint(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update_item_endpoint(item_id: int, name: str, description: str, db: AsyncSession = Depends(get_db)):
    return await update_item(db, item_id, name, description)

@app.delete("/items/{item_id}")
async def delete_item_endpoint(item_id: int, db: AsyncSession = Depends(get_db)):
    await delete_item(db, item_id)
    return {"message": "Item deleted successfully"}
