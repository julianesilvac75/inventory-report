import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".json") is not True:
            raise ValueError("Arquivo inválido")
            return

        with open(file) as json_file:
            products_list = json.load(json_file)

        return products_list
