from fastapi import APIRouter, HTTPException

from app.models.models import Project
from app.services.Service import Service

router = APIRouter()
service = Service()


@router.post("/", response_model=Project)
async def create_project(project: Project):
    service.projects_db.append(project)
    return project


@router.get("/{project_id}", response_model=Project)
async def get_project(project_id: int):
    project = service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/{project_id}/budget", response_model=float)
async def get_budget(project_id: int):
    project = service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.budget


@router.put("/{project_id}/budget", response_model=Project)
async def edit_budget(project_id: int, new_budget: float):
    project = service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    project.budget = new_budget
    return project


@router.get("/{project_id}/status", response_model=str)
async def get_project_status(project_id: int):
    project = service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.status


@router.put("/{project_id}/status", response_model=Project)
async def edit_project_status(project_id: int, new_status: str):
    project = service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    project.status = new_status
    return project
