import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        with open(path, encoding="utf-8") as file:
            if path.endswith('csv'):
                file_csv = csv.DictReader(file)
                data = list(file_csv)

        if type == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
