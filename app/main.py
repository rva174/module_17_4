from fastapi import FastAPI
from app.routers.user import user
from app.routers.task import task


# import logging
#
# logging.getLogger("uvicorn").handlers.clear()


app = FastAPI()

# Создание таблиц
# Base.metadata.create_all(bind=engine)



@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user)
app.include_router(task)

# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run(app,host='0.0.0.0', port=8000)

# pip install alembic   # установка alembic
# alembic init app/migrations    # создание начальных файлоф
# alembic revision --autogenerate -m "Initial migration"    #После настройки alembic и env
# alembic upgrade head