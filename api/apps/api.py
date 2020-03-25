from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[App], response_description="Return a list of applications")
def list_apps():
    return query(tables.App)


@router.post("/", response_model=App, response_description="Create a new app.")
def create_app(app_in: App):
    return create(tables.App, app_in)


@router.get("/{id}", response_model=App)
def get_app(id: str):
    return get_or_error(tables.App, id, "App not found")


@router.put("/{id}", response_model=App)
def update_app(*, id: str, app_in: App):
    return update(tables.App, id, app_in)


@router.delete("/{id}", response_model=App)
def delete_app(id: str):
    return delete(tables.App, id)


@router.get("/{id}/{environment}", response_model=AppInstance)
def get_app_instance(id: str):
    app = get_or_error(tables.App, id)
    return app


@router.put("/{id}/{environment}", response_model=AppInstance)
def update_app_instance(*, id: str, app_in: App):
    app = get_or_error(tables.App, id)

    app_data = db_process_input(app_in, app)
    if app_data:
        return update(tables.App, app=app, data=app_data)
    else:
        return app


@router.delete("/{id}/{environment}", response_model=AppInstance)
def delete_app(id: str):
    app = get_or_error(tables.App, id)
    return delete(app)
