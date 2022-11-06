import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, type):
        if file.endswith(".csv"):
            products_list = cls.get_csv_file(file)

        if file.endswith("json"):
            products_list = cls.get_json_file(file)

        if file.endswith("xml"):
            products_list = cls.get_xml_file(file)

        if type == "simples":
            return SimpleReport.generate(products_list)
        elif type == "completo":
            return CompleteReport.generate(products_list)
        else:
            raise ValueError

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
