from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class OperationKind(str, Enum):
	INCOME = 'income'
	OUTCOME =	'outcome'


class OperationBase(BaseModel):
	date: date
	kind: OperationKind
	amount: int
	description: Optional[str]


class Operation(OperationBase):
	id: int

	class Config:
		orm_mode = True


class OperationCreate(OperationBase):
	pass


class OperationUpdate(OperationBase):
	pass
