import logging
from fastapi import FastAPI, HTTPException
from prisma import Prisma
from pydantic import BaseModel, Field
from typing import List, Optional

# 1. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nexus-api")

app = FastAPI(title="Nexus Data API", description="Enterprise Data Layer")
db = Prisma()

class ProjectCreate(BaseModel):
    """Data model for creating a new project."""
    name: str = Field(..., min_length=1, description="The unique name of the project")
    description: Optional[str] = Field(None, description="Optional project details")

@app.on_event("startup")
async def startup():
    """Connect to the database on startup."""
    logger.info("Connecting to the database...")
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    """Disconnect from the database on shutdown."""
    logger.info("Closing database connection...")
    await db.disconnect()

@app.get("/projects", response_model=List[dict])
async def get_projects():
    """Retrieve all projects from the database."""
    logger.info("Fetching all projects")
    return await db.project.find_many()

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