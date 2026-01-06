from pytz import timezone
from typing import Optional, List
from datetime import datetime, timedelta
from pydantic import EmailStr

from jose import jwt
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserModel
from core.configs import settings
from core.security import check_password


# Endpoint for creating the access token.
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/token'
)


# A function that authenticates a user based on the email and password provided.
async def authenticate_user(email: EmailStr, password: str, db: AsyncSession) -> Optional[UserModel]:
    async with db as session:
        query = select(UserModel).filter(UserModel.email == email)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not check_password(password, user.password):
            return None
        
        return user
    

# function to create the JWT token with some specific information
def _create_token(type_token: str, lifetime: timezone, sub: str) -> str:
    payload = {}
    sp = timezone("America/Sao_Paulo")
    expire = datetime.now(tz=sp) + lifetime

    payload['type'] = type_token
    payload['exp'] = expire
    payload['iat'] = datetime.now(tz=sp)
    payload['sub'] = str(sub)

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        settings.ALGORITHM
    )

# This function will actually create our access token for the user.
def create_access_token(sub: str) -> str:
    return _create_token(
        type_token='access_token',
        lifetime=timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )

