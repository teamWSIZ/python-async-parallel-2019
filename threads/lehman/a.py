from dataclasses import dataclass
from typing import Dict

m = {}
m['a'] = 11
m['account12'] = 33

print(m)
print(m.__len__())

# właściwa deklaracja, z typem
mm: Dict[int, str] = {}

@dataclass
class AA:
    aa : int

@dataclass
class Account:
  account_no : int
  secret : str
  funds : int

a = Account(1, 'aaa', 10)
b = Account(2, '111', 10)

print([a,b])

class Lehman:
  accounts: Dict[int, Account] = {}

  def create_account(self, secret: str):
      next_id = self.accounts.__len__() + 1
      self.accounts[next_id] = Account(next_id, secret, 10)

