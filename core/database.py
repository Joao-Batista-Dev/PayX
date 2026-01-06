from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine

from core.configs import settings


# asynchronous connection to the database
engine: AsyncEngine = create_async_engine(settings.DATABASE_URL)

# creating a database session
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)