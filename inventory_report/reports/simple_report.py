from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def oldest_date_fabrication(cls, list):
        return min([item["data_de_fabricacao"] for item in list])

    @classmethod
    def closet_date_fabrication(cls, list):
        date_now = datetime.today()

        return min([item["data_de_validade"] for item in list
                    if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                    > date_now])

    @classmethod
    def most_common_company(cls, list):

        return Counter(item["nome_da_empresa"]
                       for item in list).most_common(1)[0][0]

    @classmethod
    def generate(cls, list):
        oldest_date = cls.oldest_date_fabrication(list)
        closet_date = cls.closet_date_fabrication(list)
        company_bigger_stock = cls.most_common_company(list)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closet_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
