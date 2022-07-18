from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class log:
    employeeId:str
    employeeName:str
    level:str
    weight:float
    money:int

@dataclass
class Account:
    accountId:str
    kind:str
    accountName:str
    budget:int
    expenditure:int = 0
    balance:int = 0
    histroy_log:List = field(default_factory=list)

    def withdraw(self, payRoll, payAccountInfo_i):
        self.expenditure += payAccountInfo_i.money
        self.balance = self.budget - self.expenditure
        l = log(employeeId=payRoll.employeeId, employeeName=payRoll.employeeName, level=payRoll.level, weight=payAccountInfo_i.weight, money=payAccountInfo_i.money)
        self.histroy_log.append(l)


@dataclass
class AccountDataSet:
    data_set:Dict
