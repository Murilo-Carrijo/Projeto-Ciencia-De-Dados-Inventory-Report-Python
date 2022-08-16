from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def get_qty_products_by_company(products):
        companies = Counter(product['nome_da_empresa'] for product in products)
        return companies.most_common()

    @classmethod
    def generate(self, products):
        companies = self.get_qty_products_by_company(products)
        simple_report = super().generate(products)
        complete_report = ""
        for name, qty in companies:
            complete_report += f"- {name}: {qty}\n"
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{complete_report}"
        )
