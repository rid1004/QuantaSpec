from fastapi import APIRouter
from sqlalchemy import text
from src.quantaspec.app.db.session import SessionDep
router = APIRouter(tags=["health"])

@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/health/db")
async def health_db(session: SessionDep) -> dict[str, str]:
    result = await session.execute(text("SELECT version();"))
    version = result.scalar_one()
    ext = await session.execute(
        text("SELECT extname FROM pg_extension WHERE extname = 'vector';")
    )
    has_vector = ext.scalar_one_or_none() is not None
    return {
        "database": "connected",
        "version": version.split(",")[0],
        "pgvector": "installed" if has_vector else "missing",
    }