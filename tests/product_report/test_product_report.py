import datetime
from inventory_report.inventory.product import Product

product_string_mock = (
    "O produto farinha fabricado em 01-05-2021 por Farinini com validade até "
    "02-06-2023 precisa ser armazenado ao abrigo de luz."
    )


def test_relatorio_produto():
    new_product = Product(
        id=1,
        nome_do_produto="farinha",
        nome_da_empresa="Farinini",
        data_de_fabricacao="01-05-2021",
        data_de_validade="02-06-2023",
        numero_de_serie="123456",
        instrucoes_de_armazenamento="ao abrigo de luz",
    )

    assert str(new_product.__repr__()) == product_string_mock
