from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def company_inventory(cls, list):
        inventory = {}
        for item in list:
            if item["nome_da_empresa"] not in inventory:
                inventory[item["nome_da_empresa"]] = 0
            inventory[item["nome_da_empresa"]] += 1

        return inventory

    @classmethod
    def format_inventory(cls, list):
        inventory = cls.company_inventory(list)

        formated_str = ''
        for item in inventory.items():
            formated_str += f"- {item[0]}: {item[1]}\n"
        return formated_str

    @classmethod
    def generate(cls, list):
        oldest_date = cls.oldest_date_fabrication(list)
        closet_date = cls.closet_date_fabrication(list)
        company_bigger_stock = cls.most_common_company(list)
        company_products_inventory = cls.format_inventory(list)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closet_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}\n"
            f"Produtos estocados por empresa:\n{company_products_inventory}"
        )
