from typing import List

from fastapi import APIRouter, HTTPException

from api.core.db_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/",
    response_model=List[Repository],
    response_description="Return a list of repositorys",
)
def list_repositories():
    return query(tables.Repository)


@router.post(
    "/",
    response_model=Repository,
    status_code=201,
    response_description="Create a new repository.",
)
def create_repository(repo_in: Repository):
    return create(tables.Repository, repo_in)


@router.get("/{id}", response_model=Repository)
def get_repository(id: str):
    return get_or_error(tables.Repository, id)


@router.delete("/{id}", status_code=204)
def delete_repository(id: str):
    delete(tables.Repository, id)
