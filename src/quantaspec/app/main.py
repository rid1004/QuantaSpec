from fastapi import Depends, FastAPI

from quantaspec.app.core.config import Settings,get_settings


app = FastAPI(title='AI QuantaSpec')


@app.get('/')
async def root(settings: Settings = Depends(get_settings)):
    return {'message': 'Welecome to QuntaSpec'}


@app.get('/health')
async def health(settings: Settings = Depends(get_settings)):
    return {'status':"ok" , 'app': settings.APP_NAME}