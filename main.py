import logging
from fastapi import FastAPI, HTTPException
from prisma import Prisma
from pydantic import BaseModel, Field
from typing import List, Optional
from contextlib import asynccontextmanager

# 1. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nexus-api")

# initialize DB client and API app
db = Prisma()

# manage DB connection lifecycle (startup / shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Connecting to DB...")
    await db.connect()
    yield
    logger.info("Disconnecting DB...")
    await db.disconnect()
# initialize DB client and API app
app = FastAPI(lifespan=lifespan)

# request schema for creating a project (input validation)
class ProjectCreate(BaseModel):
    """Data model for creating a new project."""
    name: str = Field(..., min_length=1, description="The unique name of the project")
    description: Optional[str] = Field(None, description="Optional project details")

# fetch all projects from DB
@app.get("/projects")
async def get_projects():
    projects = await db.project.find_many()
    return [p.model_dump() for p in projects]

# create new project entry in DB
@app.post("/projects")
async def create_project(project: ProjectCreate):
    """Create a new project entry."""
    logger.info(f"Creating project: {project.name}")
    try:
        new_project = await db.project.create(
            data={'name': project.name, 'description': project.description}
        )
        return new_project
    except Exception as e:
        logger.error(f"Error creating project: {e}")
        raise HTTPException(status_code=500, detail="Database Error")