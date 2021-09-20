from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import UserCreate, Token, User
from services.auth import AuthService, get_current_user


router = APIRouter(
	prefix='/auth',
	tags=['auth'],
)


@router.post('/sign-up', response_model=Token)
def sign_up(
	user_data: UserCreate, 
	service: AuthService = Depends(),
	):
	'''
	Sign Up
	'''
	return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(
	form_data: OAuth2PasswordRequestForm = Depends(),
	service: AuthService = Depends(),
	):
	'''
	Sign In
	'''
	return service.authenticate_user(
		form_data.username,
		form_data.password,
	)


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
	'''
	Get current user.
	'''
	return user
