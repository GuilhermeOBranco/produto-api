from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    sucesso: bool
    mensagem: Optional[str]
    data: Optional[T]
