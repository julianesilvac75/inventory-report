import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def get_csv_file(cls, file):
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')

            product_list = [row for row in reader]

        return product_list

    @classmethod
    def get_json_file(cls, file):
        with open(file) as json_file:
            products = json.load(json_file)

        return products

    @classmethod
    def get_xml_file(cls, file):
        if file.endswith("xml") is False:
            raise ValueError("Arquivo inválido")

        with open(file) as xml_file:
            products = xmltodict.parse(xml_file.read())
            xml_file.close()
            products_list = products["dataset"]["record"]

        return products_list

    @classmethod
    def get_products(cls, file):
        product_list = []

        if file.endswith("csv"):
            product_list = cls.get_csv_file(file)
        if file.endswith("json"):
            product_list = cls.get_json_file(file)
        else:
            with open(file) as xml_file:
                products = xmltodict.parse(xml_file.read())
                xml_file.close()
                product_list = products["dataset"]["record"]

        return product_list

    @classmethod
    def import_data(cls, file, type):
        product_list = cls.get_products(file)

        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
        else:
            raise ValueError


if __name__ == "__main__":
    Inventory.import_data("inventory_report/data/inventory.csv", "simples")
