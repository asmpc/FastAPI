from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import select, ScalarResult

from src.account.models import User
from src.account.schemas.user import UserCreateSchema, UserUpdateSchema


class UserRepository:
    def __init__(self, session: Session):
        self.session = session


    def create(self, user_schema: UserCreateSchema) -> User:
        user = User(
            fullname=user_schema.fullname,
            email=user_schema.email,
            sex=user_schema.sex,
        )
        self.session.add(user)
        self.session.commit()
        self.session.flush()
        return user

    def get_one(self, user_id: int) -> ScalarResult[User]:
        stm = select(User).where(User.id==user_id)
        return self.session.execute(stm).scalar()

    def check_exists_email(self, email: str = None) -> ScalarResult[User]:
        stm = select(User).where(User.email == email)
        return self.session.execute(stm).scalar()

    def check_exists_user_id(self, user_id: int = None) -> ScalarResult[User]:
        stm = select(User).where(User.id == user_id)
        return self.session.execute(stm).scalar()


    def get_all(self) -> ScalarResult[User]:
        stm = select(User)
        return self.session.execute(stm).scalars()

    def update(
            self,
            user: User,
            user_schema: UserUpdateSchema,
    ) -> User:
        for name, value in user_schema.model_dump().items():
            setattr(user, name, value)
        self.session.commit()
        self.session.flush()
        return user


    def remove(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()


