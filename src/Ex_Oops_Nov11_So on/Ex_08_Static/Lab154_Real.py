class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")
class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TestC1:

    def runTestC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:

    def runTestC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

tc1 = TestC1()
tc2 = TestC1()
tc1.runTestC()
tc2.runTestC()