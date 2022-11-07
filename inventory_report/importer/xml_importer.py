import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".xml") is not True:
            raise ValueError("Arquivo inválido")
            return

        with open(file) as xml_file:
            products = xmltodict.parse(xml_file.read())
            xml_file.close()
            products_list = products["dataset"]["record"]

        return products_list
