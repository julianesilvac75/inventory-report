import csv
import json
import xmltodict

# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, type):
        products_list = cls.get_products(file)

        if type.lower() == "simples":
            report = SimpleReport.generate(products_list)
        else:
            report = CompleteReport.generate(products_list)

        return report

    @classmethod
    def get_products(cls, file):
        products = []

        if file.endswith("csv"):
            products = cls.get_csv_file(file)
        if file.endswith("json"):
            products = cls.get_json_file(file)
        else:
            products = cls.get_xml_file(file)

        return products

    @classmethod
    def get_csv_file(cls, file):
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            products_list = [row for row in reader]

        return products_list

    @classmethod
    def get_json_file(cls, file):
        with open(file) as json_file:
            products_list = json.load(json_file)

        return products_list

    @classmethod
    def get_xml_file(cls, file):
        with open(file) as xml_file:
            products = xmltodict.parse(xml_file.read())
            xml_file.close()
            products_list = products["dataset"]["record"]

        return products_list


if __name__ == "__main__":
    Inventory.import_data("inventory_report/data/inventory.xml", "simples")
