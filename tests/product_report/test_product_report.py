from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_da_empresa="Xablau",
        nome_do_produto="molho de tomate",
        data_de_fabricacao="12/08/2022",
        data_de_validade="12/08/2023",
        numero_de_serie="123456789XB",
        instrucoes_de_armazenamento="Utilizar todo o conteudo"
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
