from behave import *
from unittest.mock import MagicMock
from main.model.user import User
from main.model.role import Role
from main.model.account import Account
from main.biz.account_manager import AccountManager
from main.db.dao import DAO


@Given('Create AccountManager instance')
def create_account_manager(context):
    account_manager = AccountManager()
    context.account_manager = account_manager


@Given('We have user with name {user_name}')
def step_create_user(context, user_name):
    context.user = User(1, user_name, Role(999, "regular_user"))


@Given('{user_name} has account number: {source_account_number} with amount: {source_amount}')
def step_add_source_account(context, user_name, source_account_number, source_amount):
    context.source_account_number = source_account_number
    context.source_account = Account(source_account_number, float(source_amount), context.user)


@Given('We have account number: {dest_account_number} with amount: {dest_amount}')
def step_add_dest_account(context, dest_account_number, dest_amount):
    context.dest_account = Account(dest_account_number, float(dest_amount), context.user)


@When('User makes internal payment from acc:{source_account_number} to acc:{dest_account_number} with amount:{amount}')
def step_make_internal_payment(context, source_account_number, dest_account_number, amount):
    context.account_manager.alt_internal_payment(context.user, "desc", float(amount),
                                                 context.source_account,
                                                 context.dest_account)


@When('User makes payment in with amount:{amount}')
def step_make_payment_in(context, amount):
    DAO.find_user_by_name = MagicMock(return_value=context.user)
    DAO.find_account_by_id = MagicMock(return_value=context.source_account)
    context.account_manager.payment_in(context.user, "desc", float(amount), context.source_account_number)


@When('User makes payment out with amount:{amount}')
def step_make_payment_out(context, amount):
    DAO.find_user_by_name = MagicMock(return_value=context.user)
    DAO.find_account_by_id = MagicMock(return_value=context.source_account)
    context.account_manager.payment_out(context.user, "desc", float(amount), context.source_account_number)


@Then('{user_name} account should have {expected_amount}')
def step_get_expected(context, user_name, expected_amount):
    context.expected_amount = expected_amount


@Then('Expected and calculated amounts should be equal')
def step_expected_account_amount(context):
    source_equals = float(context.expected_amount) == context.source_account.get_amount()
    assert source_equals is True


@Then('Account {source_account_number} should have {source_expected_amount} '
      'and account {dest_account_number} should have {dest_expected_amount}')
def step_get_expected_for_both(context, source_account_number, source_expected_amount,
                               dest_account_number, dest_expected_amount):
    context.source_expected_amount = source_expected_amount
    context.dest_expected_amount = dest_expected_amount


@Then('Expected and calculated amounts should be equal for both')
def step_expected_account_amount_for_both(context):
    source_equals = float(context.source_expected_amount) == context.source_account.get_amount()
    assert source_equals is True
    dest_equals = float(context.dest_expected_amount) == context.dest_account.get_amount()
    assert dest_equals is True
