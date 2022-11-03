from inventory_report.inventory.product import Product
import datetime


product_mock = {
    "id": 1,
    "nome_da_empresa": "Mercado",
    "nome_do_produto": "Leite",
    "data_de_fabricacao": datetime.date(2022, 10, 1),
    "data_de_validade": datetime.date(2022, 10, 10),
    "numero_de_serie": "123456",
    "instrucoes_de_armazenamento": "Guardar na geladeira",
}


def test_cria_produto():
    new_product = Product(
        product_mock["id"],
        product_mock["nome_do_produto"],
        product_mock["nome_da_empresa"],
        product_mock["data_de_fabricacao"],
        product_mock["data_de_validade"],
        product_mock["numero_de_serie"],
        product_mock["instrucoes_de_armazenamento"],
    )

    print(new_product)

    assert hasattr(new_product, "id") is True
    assert new_product.id == product_mock["id"]
    assert type(new_product.id) is int

    assert hasattr(new_product, "nome_do_produto") is True
    assert new_product.nome_do_produto == product_mock["nome_do_produto"]
    assert type(new_product.nome_do_produto) is str

    assert hasattr(new_product, "nome_da_empresa")
    assert new_product.nome_da_empresa == product_mock["nome_da_empresa"]
    assert type(new_product.nome_da_empresa) is str

    assert hasattr(new_product, "data_de_fabricacao") is True
    assert new_product.data_de_fabricacao == product_mock["data_de_fabricacao"]
    assert type(new_product.data_de_fabricacao) is str

    assert hasattr(new_product, "data_de_validade") is True
    assert new_product.data_de_validade == product_mock["data_de_validade"]
    assert type(new_product.data_de_validade) is str

    assert hasattr(new_product, "numero_de_serie") is True
    assert new_product.numero_de_serie == product_mock["numero_de_serie"]
    assert type(new_product.numero_de_serie) is str

    assert hasattr(new_product, "instrucoes_de_armazenamento") is True
    assert (
        new_product.instrucoes_de_armazenamento
        == product_mock["instrucoes_de_armazenamento"]
        )
    assert type(new_product.instrucoes_de_armazenamento) is str
