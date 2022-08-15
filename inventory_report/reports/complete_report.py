from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def get_qty_products_by_company(products):
        companies = Counter(product['nome_da_empresa'] for product in products)
        return companies.most_common()

    @classmethod
    def generate(self, products):
        complete_report = self.get_qty_products_by_company(products)
        simple_report = super().generate(products)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"- {complete_report[0][0]}: {complete_report[0][1]}\n"
            f"- {complete_report[1][0]}: {complete_report[1][1]}\n"
            f"- {complete_report[2][0]}: {complete_report[2][1]}\n"
        )
