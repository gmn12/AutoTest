# from day01.util import GetCsv

class GetCsv:
    @staticmethod
    def getCsv(path):
        with open(path,'r',encoding="utf-8") as file:
            workbook = file.read()
            data = [(i.split(',')) for i in workbook.split('\n')]
        return data[1:]
