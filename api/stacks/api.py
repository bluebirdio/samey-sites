from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Stack], response_description="Return a list of stacks")
def list_stacks():
    return query(tables.Stack)


@router.post("/", response_model=Stack, response_description="Create a new stack.")
def create_stack(stack_in: Stack):
    return create(tables.Stack, stack_in)


@router.put("/{id}", response_model=Stack)
def update_stack(id: str, stack_in: Stack):
    return update(tables.Stack, id, stack_in)


@router.get("/{id}", response_model=Stack)
def get_stack(id: str):
    return get_or_error(tables.Stack, id, "Stack not found")


@router.delete("/{id}", response_model=Stack)
def delete_stack(id: str):
    return delete(tables.Stack, id)