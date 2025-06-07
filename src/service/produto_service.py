from typing import List

from schema.request.cadastro_produto_schema_request import ProdutoRequestSchema


class ProdutoService:
    def __init__(self):
        self._produtos: List[ProdutoRequestSchema] = []

    def inserir_produto(self, produto: ProdutoRequestSchema):
        self._produtos.append(produto)

    def obter_produtos(self) -> List[ProdutoRequestSchema]:
        return self._produtos

    def atualizar_produto(
        self, nomeProduto: str, produto_atualizado: ProdutoRequestSchema
    ) -> bool:
        if nomeProduto in self._produtos:
            self._produtos[nomeProduto] = produto_atualizado
            return True
        return False


produto_service = ProdutoService()


def get_produto_service():
    return produto_service
