import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def format_data_xml(self, root):
        data = []
        info_dict = {}
        for i in range(len(root)):
            for info in root[i]:
                info_dict[info.tag] = info.text
            data.append(info_dict)
            info_dict = {}
        return data

    @classmethod
    def import_data(self, path, type):
        with open(path, encoding="utf-8") as file:
            if path.endswith('csv'):
                file_csv = csv.DictReader(file)
                data = list(file_csv)
            if path.endswith('json'):
                data = json.load(file)
            if path.endswith('xml'):
                tree = ET.parse(path)
                root = list(tree.getroot())
                data = self.format_data_xml(root)

        if type == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
