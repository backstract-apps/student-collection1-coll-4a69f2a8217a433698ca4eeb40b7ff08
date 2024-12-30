from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - student-collection1-coll-4a69f2a8217a433698ca4eeb40b7ff08',debug=False,docs_url='/exciting-kowalevski-c033b3bac6a911ef952c0242ac12000385/docs',openapi_url='/exciting-kowalevski-c033b3bac6a911ef952c0242ac12000385/openapi.json')

app.include_router(router, prefix='/exciting-kowalevski-c033b3bac6a911ef952c0242ac12000385/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()