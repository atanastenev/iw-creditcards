#-----------------------------------------------------------------------
# creditcard.py
# Authors: Nasko Tenev
#-----------------------------------------------------------------------

class CreditCard:

    def __init__(self, card):
        # d = stringdate.split('-')
        self._name = card[0]
        self._bank = card[1]
        self._annualfee = card[2]
        self._creditscore = card[3]
        self._bonus = card[4]
        self._pros = card[5]
        self._cons = card[6]
        self._details = card[7]
        self._link = card[8]

    # def __str__(self): 
    #     return self._month + " " + self._day + " "+ self._year
        
    def get_name(self):
        return self._name
    def get_bank(self):
        return self._bank
    def get_afee(self):
        return self._annualfee 
    def get_creditscore(self):
        return self._creditscore 
    def get_bonus(self):
        return self._bonus
    def get_pros(self):
        return self._pros 
    def get_cons(self):
        return self._cons
    def get_details(self):
        return self._details
    def get_link(self):
        return self._link
    def to_string(self): 
        return self._name + " " + self._bank + " "+ self._link