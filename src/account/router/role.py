from fastapi import APIRouter


router = APIRouter(
    prefix="/roles",
    tags=["Account"],
)


# @router.get("/")
# def read_roles():
#     return [{"name": "Admin"}, {"name": "Moderator"}]
