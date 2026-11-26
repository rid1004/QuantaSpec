from fastapi import Depends, FastAPI
from sqlalchemy import text
from quantaspec.app.core.config import Settings,get_settings
from quantaspec.app.db.session import SessionDep

app = FastAPI(title='AI QuantaSpec')


@app.get('/')
async def root(settings: Settings = Depends(get_settings)):
    return {'message': 'Welecome to QuntaSpec'}


@app.get('/health')
async def health(settings: Settings = Depends(get_settings)):
    return {'status':"ok" , 'app': settings.APP_NAME}

@app.get("/health/db")
async def health_db(session: SessionDep) -> dict[str, str]:
    result = await session.execute(text("SELECT version();"))
    version = result.scalar_one()

    ext = await session.execute(
        text("SELECT extname FROM pg_extension WHERE extname = 'vector';")
    )
    has_vector = ext.scalar_one_or_none() is not None

    return {
        "database": "connected",
        "version": version,
        "has_vector": "yes" if has_vector else "no",
    }