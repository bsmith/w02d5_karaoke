class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.paid_fee = False
    
    def can_afford_fee(self, fee_amount):
        return fee_amount <= self.wallet
    
    def pay_fee(self, fee_amount):
        if self.can_afford_fee(fee_amount):
            self.wallet -= fee_amount
            self.paid_fee = True
        assert self.wallet > 0