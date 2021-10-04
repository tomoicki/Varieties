from behave import *
from unittest.mock import MagicMock
from main.model.user import User
from main.model.role import Role
from main.model.account import Account
from main.db.dao import DAO
from main.biz.account_manager import AccountManager
from main.biz.interest_operator import InterestOperator


@Given('Create InterestOperator instance')
def create_interest_operator(context):
    context.interest_operator = InterestOperator(AccountManager())


@Given('We have user with the name {user_name}')
def step_create_user(context, user_name):
    context.user = User(1, user_name, Role(999, "regular_user"))


@Given('He/She has account with amount: {source_amount}')
def step_add_account(context, source_amount):
    context.source_account = Account(1, float(source_amount), context.user)


@When('The interest is calculated')
def step_calculate_interest(context):
    DAO.find_user_by_name = MagicMock(return_value=context.user)
    DAO.find_account_by_id = MagicMock(return_value=context.source_account)
    context.interest_operator.count_interest_for_account(context.source_account)


@Then('His/Her account should have: {expected_amount}')
def step_get_expected(context, expected_amount):
    context.expected_amount = expected_amount


@Then('Calculated amount should equal expected amount')
def step_is_it_equal(context):
    source_equals = float(context.expected_amount) == context.source_account.get_amount()
    assert source_equals is True
