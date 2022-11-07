import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".csv") is not True:
            raise ValueError("Arquivo inválido")
            return

        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            products_list = [row for row in reader]

        return products_list
