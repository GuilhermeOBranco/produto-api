from pydantic import BaseModel as SCBaseModel


class ProdutoRequestSchema(SCBaseModel):
    nomeProduto: str
    quantidade: int
