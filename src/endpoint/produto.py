from typing import List
from fastapi import APIRouter, Depends
from fastapi import status
from service.produto_service import ProdutoService, get_produto_service

from schema.request.cadastro_produto_schema_request import ProdutoRequestSchema


router: APIRouter = APIRouter()


@router.post(
    "/cadastrar-produto",
    status_code=status.HTTP_201_CREATED,
    response_model=ProdutoRequestSchema,
)
async def inserir_produto(
    produto: ProdutoRequestSchema,
    service: ProdutoService = Depends(get_produto_service),
):
    try:
        service.inserir_produto(produto)
        return produto
    except Exception as ex:
        print(ex)
        return status.HTTP_500_INTERNAL_SERVER_ERROR


@router.get(
    "/obter-produtos",
    status_code=status.HTTP_200_OK,
    response_model=List[ProdutoRequestSchema],
)
async def obter_produtos(service: ProdutoService = Depends(get_produto_service)):
    return service.obter_produtos()
