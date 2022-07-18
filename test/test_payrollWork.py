from payroll.payrollModel import PayRollDataSet
from payroll.payRollWork import FFixedPayInfo, FFixedPayAccountInfo, FPayRoll, PayRollAdder, FAccountDataSet
import unittest

class TestPayRollAdder(unittest.TestCase):

    def setUp(self) -> None:
        self.prds = PayRollDataSet()
        self.wl = [
            {'employeeId':'201503002', 'employeeName':'홍길동', 'level':'4급', 'date':'1월'},
            {'employeeId':'201503006', 'employeeName':'김철수', 'level':'4급', 'date':'1월'}
            ]
        self.ffpi = FFixedPayInfo()
        self.ffpai = FFixedPayAccountInfo()
        self.fpr = FPayRoll(self.ffpi, self.ffpai)

    def test_payrolladder(self):
        pra = PayRollAdder(self.prds, self.wl, self.fpr)
        dataset = pra.get_dataSet()

        print(dataset)

class TestFAccountDataSet(unittest.TestCase):

    def test_faccountDaTaSet(self):
        fads = FAccountDataSet()
        print(fads.get_data_set())

if __name__ == '__main__':

    unittest.main()