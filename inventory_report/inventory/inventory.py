import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, type):
        product_list = []

        if file.endswith("csv"):
            with open(file) as csv_file:
                reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')

                product_list = [row for row in reader]

        if file.endswith("json"):
            with open(file) as json_file:
                products = json.load(json_file)

            product_list = products

        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
        else:
            raise ValueError


if __name__ == "__main__":
    Inventory.import_data("inventory_report/data/inventory.csv", "simples")
