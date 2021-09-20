from typing import List, Optional

from fastapi import (
	APIRouter,
	Depends,
	Response,
	status,
)

from models.operations import (
	Operation, 
	OperationBase, 
	OperationCreate, 
	OperationKind, 
	OperationUpdate,
)
from models.auth import User
from services.auth import get_current_user
from services.operations import OperationsService

router = APIRouter(
	prefix='/operations',
	tags=['operations'],
)


@router.get('/', response_model=List[Operation])
def get_operations(
	kind: Optional[ OperationKind] = None,
	user: User = Depends(get_current_user),
	service: OperationsService = Depends(),
):
	'''
	Get operations list.

	- **kind**: Filter of operation type.
	'''
	return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
	operation_data: OperationCreate,
	user: User = Depends(get_current_user),
	service: OperationsService = Depends(),
):
	'''
	Create an operation.

	- **kind**: Filter of operation type.
	'''
	return service.create(user_id=user.id, operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
	operation_id: int,
	user: User = Depends(get_current_user),
	service: OperationsService = Depends(),
):
	'''
	Get an operation by id.

	- **kind**: Filter of operation type.
	'''
	return service.get(user_id=user.id, operation_id=operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
	operation_id: int,
	operation_data: OperationUpdate,
	user: User = Depends(get_current_user),
	service: OperationsService = Depends(),
):
	'''
	Update an operation by id.

	- **kind**: Filter of operation type.
	'''
	return service.update(
		user_id=user.id,
		operation_id=operation_id,
		operation_data=operation_data,
	)


@router.delete('/{operation_id}')
def delete_operation(
	operation_id: int,
	user: User = Depends(get_current_user),
	service: OperationsService = Depends(),
):
	'''
	Delete an operation by id.

	- **kind**: Filter of operation type.
	'''
	service.delete(user_id=user.id, operation_id=operation_id)
	return Response(status_code=status.HTTP_204_NO_CONTENT)
