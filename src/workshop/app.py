import uvicorn
from fastapi import FastAPI
from settings import settings
from api import router


tags_metadata = [
	{
		'name': 'auth',
		'description': 'Authorisation & registration',
	},
	{
		'name': 'operations',
		'description': 'Work with operations',
	},
	{
		'name': 'reports',
		'description': 'Import & export of reports',
	},
]


app = FastAPI(
	title='My first FastAPI project',
	description='Personal income and expense tracking service',
	version='1.0.0',
	openapi_tags=tags_metadata,
)

app.include_router(router)


if __name__ == '__main__':
	uvicorn.run(
		'app:app', 
		host=settings.server_host,
		port=settings.server_port,
		reload=True
	)
