from payroll.payrollModel import PayInfo, PayAccountInfo, PayRoll
from payroll.accountModel import Account, AccountDataSet
from pathlib import Path
import pandas as pd

class FFixedPayInfo:

    def __init__(self):
        # F:\회사\220715\11. 인건비\test
        file_path = Path('F:').joinpath('회사', '220715', '11. 인건비', 'test', '급여스케쥴.csv')
        self.df = pd.read_csv(file_path, encoding='utf-8')
        self.df['employeeId'] = self.df['employeeId'].astype(str)

    def get_payinfo(self, employeeId, date):
        con1 = (self.df['employeeId'] == employeeId)
        con2 = (self.df['date'] == date)
        queried_df=self.df.loc[con1&con2]
        dataList = queried_df.loc[:,'gibongub':].to_dict(orient='records')
        return PayInfo(**dataList[0])


class FFixedPayAccountInfo:

    def __init__(self): 
        # F:\회사\220715\11. 인건비\test
        file_path = Path('F:').joinpath('회사', '220715', '11. 인건비', 'test', '지출계정스케쥴.csv')
        self.df = pd.read_csv(file_path, encoding='utf-8')
        self.df['employeeId'] = self.df['employeeId'].astype(str)

    def get_payAccountInfo(self, employeeId, date):

        con1 = self.df.loc[:, 'employeeId'] == employeeId
        con2 = self.df.loc[:, 'date'] == date
        queried_df=self.df.loc[con1&con2]
        dataList = queried_df.loc[:,'accountId':].to_dict(orient='records')
        return [PayAccountInfo(**i) for i in dataList]

class FPayRoll:

    def __init__(self, FPayInfo, FPayAccountInfo):
        self.fpi = FPayInfo
        self.fpai = FPayAccountInfo

    def create_payroll(self, employeeId, employeeName, level, date):
        pi = self.fpi.get_payinfo(employeeId, date)
        pai = self.fpai.get_payAccountInfo(employeeId, date)
        return PayRoll(employeeId, employeeName, level, date, pi, pai)

class PayRollAdder:

    def __init__(self, payRollDataSet, working_list, FPayRoll):
        self.payRollDataSet = payRollDataSet
        self.working_list = working_list
        self.FPayRoll = FPayRoll

    def add_payRoll(self):
        for work in self.working_list:
            payRoll = self.FPayRoll.create_payroll(work['employeeId'], work['employeeName'], work['level'], work['date'])
            self.payRollDataSet.data_set.append(payRoll)

    def get_dataSet(self):
        self.add_payRoll()
        return self.payRollDataSet


class FAccountDataSet:

    def __init__(self):
        file_path = Path('F:').joinpath('회사', '220715', '11. 인건비', 'test', '계정정보.csv')
        self.datalist = pd.read_csv(file_path, encoding='utf-8').to_dict(orient='records')

    def get_data_set(self):
        container = dict()
        for i in self.datalist:
            container[i['accountId']] = Account(**i)
        return AccountDataSet(container)