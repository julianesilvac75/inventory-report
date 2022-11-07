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
        product_list = []

        if file.endswith("csv"):
            with open(file) as csv_file:
                products = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )

                product_list = [row for row in products]

        if file.endswith("json"):
            with open(file) as json_file:
                products = json.load(json_file)
                product_list = products

        if file.endswith("xml"):
            with open(file) as xml_file:
                products = xmltodict.parse(xml_file.read())
                xml_file.close()
                product_list = products["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
        else:
            products = cls.get_xml_file(file)

        return products


if __name__ == "__main__":
    Inventory.import_data("inventory_report/data/inventory.xml", "simples")
