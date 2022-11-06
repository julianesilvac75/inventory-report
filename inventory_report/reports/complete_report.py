from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        report = "Produtos estocados por empresa:\n"
        products_by_company = super().get_products_by_company(list)

        for company, quantity in products_by_company.items():
            report += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n" +
            report
            )


LIST = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Empresa A",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2022-05-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Empresa B",
        "data_de_fabricacao": "2022-03-04",
        "data_de_validade": "2023-01-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Empresa A",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-01-10",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Empresa C",
        "data_de_fabricacao": "2022-07-04",
        "data_de_validade": "2023-07-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]

if __name__ == "__main__":
    print(CompleteReport.generate(LIST))
