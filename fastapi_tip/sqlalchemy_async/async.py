from sqlalchemy.ext.asyncio import AsyncEngine , AsyncSession , create_async_engine
from sqlalchemy.ext.declarative import declarative_base
'''
setdb
참고 :
https://blog.neonkid.xyz/269
https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html
'''

DATABASE_URL = 'YOURDBURL'
engine = create_async_engine(DATABASE_URL , echo =True)
Base = declarative_base()
SessionLocal = AsyncSession(bind=engine)
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)