from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[User], response_description="Return a list of users")
def list_users():
    return query(tables.User)


@router.post("/", response_model=User, response_description="Create a new user.")
def create_user(user_in: User):
    return create(tables.User, user_in)


@router.get("/{id}", response_model=User)
def get_user(id: str):
    return get_or_error(tables.User, id, "User not found")


@router.delete("/{id}", response_model=User)
def delete_user(id: str):
    return delete(tables.User, id)
