from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_da_empresa="Xablau",
        nome_do_produto="molho de tomate",
        data_de_fabricacao="12/08/2022",
        data_de_validade="12/08/2023",
        numero_de_serie="123456789XB",
        instrucoes_de_armazenamento="Utilizar todo o conteudo"
    )
    assert product.id == 1
    assert product.nome_da_empresa == "Xablau"
    assert product.nome_do_produto == "molho de tomate"
    assert product.data_de_fabricacao == "12/08/2022"
    assert product.data_de_validade == "12/08/2023"
    assert product.numero_de_serie == "123456789XB"
    assert product.instrucoes_de_armazenamento == "Utilizar todo o conteudo"
