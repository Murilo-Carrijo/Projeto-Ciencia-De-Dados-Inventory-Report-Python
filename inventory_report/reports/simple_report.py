from datetime import datetime


class SimpleReport:

    def oldest_manufacturing(products):
        oldest_product = datetime.today().strftime("%Y-%m-%D")
        for product in products:
            if product["data_de_fabricacao"] < oldest_product:
                oldest_product = product["data_de_fabricacao"]
        return oldest_product

    def shelf_life(products):
        today = datetime.today().strftime("%Y-%m-%D")
        shelf_product = "2025-10-17"
        for product in products:
            if product["data_de_validade"] > today:
                if product["data_de_validade"] < shelf_product:
                    shelf_product = product["data_de_validade"]
        return shelf_product

    def company_with_more_products(products):
        companies = list(product['nome_da_empresa'] for product in products)
        print(companies)
        return max(companies, key=companies.count)

    def generate(products):
        manufacturing = SimpleReport.oldest_manufacturing(products)
        shelf = SimpleReport.shelf_life(products)
        company = SimpleReport.company_with_more_products(products)
        return(
           f"Data de fabricação mais antiga: {manufacturing}\n"
           f"Data de validade mais próxima: {shelf}\n"
           f"Empresa com mais produtos: {company}"
        )