from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from http import HTTPStatus

from src.account.schemas.user import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from src.account.services.user import UserService, UserAlreadyExist, UserNotFound
from src.core.database import get_sync_session

router = APIRouter(
    prefix="/users",
    tags=["Account"],
)


# @router.get("/")
# def read_users():
#     return [{"name": "Rick"}, {"name": "Morty"}]


@router.post(
    path="/",
    response_model=UserResponseSchema | None,
    status_code=201,
)
def create_user(
        user_schema: UserCreateSchema,
        session: Session = Depends(get_sync_session),
):
    try:
        user_service = UserService(session)
        return user_service.create(user_schema=user_schema)
    except UserAlreadyExist:
        raise HTTPException(status_code=403, detail=f"User already exists")


@router.get(
    path="/{user_id}",
    response_model=UserResponseSchema,
    status_code=200,
)
def get_user(
        user_id: int,
        session: Session = Depends(get_sync_session),
):
    try:
        user_service = UserService(session)
        return user_service.get_one(user_id=user_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")

@router.get(
    path="/",
    response_model=list[UserResponseSchema],
    status_code=200,
)
def get_users(
        session: Session = Depends(get_sync_session),
):
    user_service = UserService(session)
    return user_service.get_all()

@router.put(
    path="/{user_id}",
    response_model=UserResponseSchema,
    status_code=200,
)
def update_user(
        user_id: int,
        user_schema: UserUpdateSchema,
        session: Session = Depends(get_sync_session),
):
    try:
        user_service = UserService(session)
        return user_service.update(user_id=user_id, user_schema=user_schema)
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")

@router.delete(
    path="/{user_id}",
    status_code=204,
)
def delete_user(
        user_id: int,
        session: Session = Depends(get_sync_session),
):
    try:
        user_service = UserService(session)
        return user_service.remove(user_id=user_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")
