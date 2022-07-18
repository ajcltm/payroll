from typing import List
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class PayInfo:

    gibongub:int
    jongsick:int
    gyotong:int
    tongsin:int
    gajock:int
    jickcheck:int
    siganwi:int
    chulnab:int
    yuncha:int
    sogub:int
    twijick:int
    total:int = 0

    def __post_init__(self):
        self.total = sum([self.gibongub, self.jongsick, self.gyotong, self.tongsin, self.gajock, self.jickcheck, self.siganwi, self.chulnab, self.yuncha, self.sogub, self.twijick])
    
@dataclass
class PayAccountInfo:

    accountId:str
    weight:float
    money:int

@dataclass
class PayRoll:
    employeeId:str
    employeeName:str
    level:str
    date:datetime
    payInfo:PayInfo
    payAccountInfo:List[PayAccountInfo]

    def pay(self, AccountDataSet):
        for payAccountInfo_i in self.payAccountInfo:
            account = AccountDataSet.data_set.get(payAccountInfo_i.accountId)
            account.withdraw(self, payAccountInfo_i)

@dataclass
class PayRollDataSet:
    data_set:List  = field(default_factory=list)