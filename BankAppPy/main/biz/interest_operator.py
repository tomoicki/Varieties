from main.model.account import Account
from main.db.dao import DAO
from main.biz.bank_history import BankHistory
from main.biz.account_manager import AccountManager
from main.model.operations.interest import Interest


class InterestOperator:
    interest_factor = 0.2
    history = BankHistory()

    def __init__(self, account_manager: AccountManager):
        self.account_manager = account_manager

    def count_interest_for_account(self, account: Account):
        amount = account.get_amount()
        if amount > 0:
            interest = amount * self.interest_factor
            user = DAO.find_user_by_name("InterestOperator")
            success = self.account_manager.payment_in(user, "desc", interest, account.get_id())
            operation = Interest(user, "desc", interest, account)
            self.history.log_operation(operation, success)
