import unittest
from payroll.accountModel import Account, AccountDataSet

class Test_account(unittest.TestCase):

    def setUp(self) -> None:
        self.raw_data = {
            'accountId' : '001',
            'kind' : '보수',
            'accountName' : '계정1_보수',
            'budget' : 1_000_000_000
        }
    
    def test_account(self):
        ac = Account(**self.raw_data)
        print(ac)

class Test_accountDataSet(unittest.TestCase):

    def setUp(self) -> None:
        self.raw_data = [
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

    def test_accountDataSet(self):

        container = dict()
        for i in self.raw_data:
            container[i['accountId']] = Account(**i)

        acd = AccountDataSet(container)
        print(acd)
    

if __name__ == '__main__':
    unittest.main()

