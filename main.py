from fastapi import FastAPI
from prisma import Prisma
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Nexus Data API")
db = Prisma()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"status": "online", "message": "Nexus Database is ready"}

@app.post("/projects")
async def create_project(project: ProjectCreate):
    new_project = await db.project.create(
        data={
            'name': project.name,
            'description': project.description
        }
    )
    return new_project

@app.get("/projects")
async def get_projects():
    projects = await db.project.find_many()
    return projects