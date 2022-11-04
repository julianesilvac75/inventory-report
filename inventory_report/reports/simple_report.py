from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, list):
        fabrication_date = cls.__get_oldest_product(list)
        validation_date = cls.__get_nearest_validation_date(list)
        company = cls.__get_company_with_most_products(list)

        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {validation_date}\n"
            f"Empresa com mais produtos: {company}"
        )

    @classmethod
    def __get_oldest_product(cls, list):
        dates = [product["data_de_fabricacao"] for product in list]

        return min(dates)

    @classmethod
    def __get_nearest_validation_date(cls, list):
        dates = []
        today = datetime.today().date()

        for product in list:
            date = datetime.strptime(product["data_de_validade"], "%Y-%m-%d")

            if date.date() > today:
                dates.append(datetime.strftime(date, "%Y-%m-%d"))

        return min(dates)

    @classmethod
    def __get_products_by_company(cls, list):
        companies = {}

        for product in list:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 0

            companies[product["nome_da_empresa"]] += 1

        return companies

    @classmethod
    def __get_company_with_most_products(cls, list):
        companies = cls.__get_products_by_company(list)

        for product in list:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 0

            companies[product["nome_da_empresa"]] += 1

        company_name = ""
        product_quantity = 0
        for company, quantity in companies.items():
            if quantity > product_quantity:
                product_quantity = quantity
                company_name = company

        return company_name


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
    print(SimpleReport.generate(LIST))
