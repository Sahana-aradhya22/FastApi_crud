from sqlalchemy.ext.asyncio import AsyncSession
from .models import Item

async def create_item(db: AsyncSession, name: str, description: str):
    item = Item(name=name, description=description)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

async def get_item(db: AsyncSession, item_id: int):
    return await db.get(Item, item_id)

async def update_item(db: AsyncSession, item_id: int, name: str, description: str):
    item = await db.get(Item, item_id)
    item.name = name
    item.description = description
    await db.commit()
    return item

async def delete_item(db: AsyncSession, item_id: int):
    item = await db.get(Item, item_id)
    await db.delete(item)
    await db.commit()
