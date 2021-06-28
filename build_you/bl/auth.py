from typing import Optional

from build_you.database import acquire_auto_commit_session as db_session
from build_you.models.user import User


async def is_valid_api_token(user_id: int, api_token: str) -> bool:
    with db_session() as session:
        res: Optional[User] = session.query(
            User
        ).filter(
            User.id == user_id
        ).first()
        return res and res.api_token and res.api_token == api_token


async def logout_user(api_token: str) -> int:
    with db_session() as session:
        res: int = session.update(
            User
        ).where(
            User.api_token == api_token
        ).values(
            api_token=''
        ).scalar()
    return res
