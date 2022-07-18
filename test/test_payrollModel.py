from payroll.payrollModel import PayInfo, PayAccountInfo, PayRoll
from payroll.accountModel import Account, AccountDataSet
import unittest
from datetime import datetime

class Test_payInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.raw_data = {
            'gibongub':3_500_000,
            'jongsick':160_000,
            'gyotong':200_000,
            'tongsin':30_000,
            'gajock':40_000,
            'jickcheck':0,
            'siganwi':510_000,
            'chulnab':0,
            'yuncha':0,
            'sogub':0,
            'twijick':500_000,
            'total':int
        }

    def test_payInfo(self):
        pi = PayInfo(**self.raw_data)
        print(pi)

class Test_payAccountInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.raw_data = {
            'accountId':'0001',
            'weight':.5,
            'money':4_950_000
        }

    def test_payInfo(self):
        pai = PayAccountInfo(**self.raw_data)
        print(pai)

class Test_payroll(unittest.TestCase):

    def setUp(self) -> None:
        self.payinfo_raw_data = {
            'gibongub':3_500_000,
            'jongsick':160_000,
            'gyotong':200_000,
            'tongsin':30_000,
            'gajock':40_000,
            'jickcheck':0,
            'siganwi':510_000,
            'chulnab':0,
            'yuncha':0,
            'sogub':0,
            'twijick':500_000,
            'total':int
        }

        self.pay_account_info_raw_data = [
            {
            'accountId':'001',
            'weight':.5,
            'money':2_475_000
        },
            {
            'accountId':'002',
            'weight':.5,
            'money':2_475_000
        }
        ]

        self.accountDataSet_raw_data = [
            {
            'accountId' : '001',
            'kind' : '보수',
            'accountName' : '계정1_보수',
            'budget' : 1_000_000_000
        },
            {
            'accountId' : '002',
            'kind' : '복리후생비',
            'accountName' : '계정1_복리',
            'budget' : 80_000_000
        }
        ]
        container = dict()
        for i in self.accountDataSet_raw_data:
            container[i['accountId']] = Account(**i)

        self.acd = AccountDataSet(container)

    def test_payroll(self):
        payroll_data = {
            'employeeId' : '2015001',
            'employeeName' : '홍길동',
            'level' : '4급',
            'date' : datetime(2022, 7, 25),
            'payInfo' : PayInfo(**self.payinfo_raw_data),
            'payAccountInfo' : [PayAccountInfo(**i) for i in self.pay_account_info_raw_data]
        }        
        pr = PayRoll(**payroll_data)
        print(pr)

        pr.pay(self.acd)

        print(self.acd)

if __name__ == '__main__':
    unittest.main()
