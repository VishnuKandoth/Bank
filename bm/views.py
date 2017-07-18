# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import *
from form import *
from .models import *


# Login, Logout functionality

def login_user(request):
    """
    authenticate user to dashboard
    """
    if request.user.is_authenticated():
        return redirect('dashboard')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('UserID')
            password = request.POST.get('Password')
            invalid = "Invalid Username / Password"
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("dashboard"))
            else:
                print ("Invalid Login Credential")
        else:
            print (form.errors)
            print ("Error in First Else ")
    else:
        form = LoginForm()
        print ("Error in second else")
    return render(request, "login.html", locals())


@login_required(login_url="/bm/")
def dashboard(request):
    """
    function defined for taking username to the dashboard
    """
    username = request.user.get_username()
    return render(request, "dashboard.html", {'username': username})


def logout_user(request):
    """
    function for logout user
    """
    logout(request)
    return render(request, "logout.html", locals())


# Bank functionalities
@login_required(login_url="/bm/")
def bank_form(request):
    """
    function defined for add bank form
    """
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
        home = request.POST.get('branch_name')
        form = BankDetail(request.POST)
        if form.is_valid():
            db_instance = Bank()
            db_instance.branch_name = form.cleaned_data.get('branch_name')
            db_instance.ifsc_code = form.cleaned_data.get('ifsc_code')
            db_instance.address = form.cleaned_data.get('address')
            db_instance.contact_no = form.cleaned_data.get('contact_no')
            db_instance.save()
            print ("Successfully Saved the data")
            return render(request, "redirect.html", locals())
        else:
            print (form.errors)
            print ("data cannot be saved .. Invalid data")
    else:
        form = BankDetail()
        print ("i am in else part")
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def bank_list(request):
    """
    defined for viewing Banklist
    """
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
        bank_table = Bank.objects.all()
        print bank_table
    else:
        banks1 = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
        bank_table = Bank.objects.filter(ifsc_code__in=banks1)
        context = {
            "bank_table": bank_table, "username": username
        }
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def edit_bank(request):
    """
    defined for editing a bank details
    """
    username = request.user.get_username()
    home = request.POST.get('ifsc_code')
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
            bank = request.POST.get('bank')
            bank_result = Bank.objects.filter(ifsc_code=bank)
            context = {
                "bank_result": bank_result,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        var = None
        if sub_user == 1:
            var = 1
            editbank = Bank.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            editbank = Bank.objects.filter(ifsc_code__in=banks)

    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def edit_bank1(request):
    """
    defined for editing a bank details from table
    """
    username = request.user.get_username()
    ifsc = request.GET.get('bank', None)
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    bank1 = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
    id = 0
    if sub_user == 1:
        id = 1
    if ifsc in list(bank1):
        id = 1
    if id == 1:
        if request.method == "POST":
            db_instance = Bank()
            db_instance.branch_name = request.POST.get('branch_name')
            db_instance.ifsc_code = request.POST.get('ifsc_code')
            db_instance.address = request.POST.get('address')
            db_instance.contact_no = request.POST.get('contact_no')
            db_instance.save()
        else:
            bank_result = Bank.objects.filter(ifsc_code=ifsc)
            context = {
                "bank_result": bank_result,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        return render(request, "error.html")


@login_required(login_url="/bm/")
def update_bank(request):
    """
    defined for updating edited details
    """
    if request.method == "POST":
            home = request.POST.get('ifsc_code')
            db_instance = Bank()
            db_instance.branch_name = request.POST.get('branch_name')
            db_instance.ifsc_code = request.POST.get('ifsc_code')
            db_instance.address = request.POST.get('address')
            db_instance.contact_no = request.POST.get('contact_no')
            db_instance.save()
            print ("Successfully Saved the data")
            return render(request, "redirect.html", locals())


# Account Functionalities
@login_required(login_url="/bm/")
def add_account(request):
    """
    defined for adding a account details
    """
    username = request.user.get_username()
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
        addaccount = EditBank(request.POST)
        if addaccount.is_valid():
            bank = request.POST.get('bank')
            context = {
                "username": username, "bank": bank,
            }
            return render(request, "dashboard.html", context)
        else:
            print ("Its in the else part")
    else:
        var = None
        if sub_user == 1:
            var = 1
            ifsc = Bank.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            ifsc = Bank.objects.filter(ifsc_code__in=banks)
            print ("Stuck over here main else part")

    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def account_list(request):
    """
    defined for viewing Accountlist
    """
    username = request.user.get_username()
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
        account_table = Account.objects.all()
    else:
        banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
        account_table = Account.objects.filter(bank_id__in=banks)
        context = {
            "account_table": account_table, 'username': username
        }
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def search_account(request):
    """
    defined for searching an account details
    """
    username = request.user.get_username()
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
            account_no = request.POST.get('account')
            account_table = Account.objects.filter(account_no=account_no)
            context = {
                "account_table": account_table,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        var = None
        if sub_user == 1:
            var = 1
            view = Account.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            view = Account.objects.filter(bank_id__in=banks)
            print ("Stuck over here main else part")
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def edit_account(request):
    """
    defined for editing a account details
    """
    username = request.user.get_username()
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
            account = request.POST.get('account')
            account_result = Account.objects.filter(account_no=account)
            context = {
                "account_result": account_result,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        var = None
        if sub_user == 1:
            var = 1
            edit = Account.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            edit = Account.objects.filter(bank_id__in=banks)
            print ("Stuck over here main else part")

    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def edit_account1(request):
    """
    defined for editing a account from table
    """
    username = request.user.get_username()
    account = request.GET.get('account', None)
    print account
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    account1 = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
    accounts = Account.objects.values_list('account_no', flat=True).filter(bank_id__in=account1)
    id = 0
    account = int(account)
    print list(accounts)
    if sub_user == 1:
        id = 1
    if account in list(accounts):
        id = 1
    print id
    if id == 1:
        if request.method == "POST":
            db_instance = Account()
            db_instance.account_no = request.POST.get('account_no')
            db_instance.account_holder = request.POST.get('account_holder')
            db_instance.bank_id = request.POST.get('bank')
            db_instance.address = request.POST.get('address')
            db_instance.contact = request.POST.get('contact')
            db_instance.account_type = request.POST.get('account_type')
            db_instance.pancard_no = request.POST.get('pancard_no')
            db_instance.save()
        else:
            account_result = Account.objects.filter(account_no=account)
            context = {
                "account_result": account_result,
                "username": username
             }
            return render(request, "dashboard.html", context)
    else:
        return render(request, "error.html")


@login_required(login_url="/bm/")
def update_account(request):
    """
    defined for updating edited details
    """
    if request.method == "POST":
            home = request.POST.get('account_no')
            db_instance = Account()
            db_instance.account_no = request.POST.get('account_no')
            db_instance.account_holder = request.POST.get('account_holder')
            db_instance.bank_id = request.POST.get('bank')
            db_instance.address = request.POST.get('address')
            db_instance.contact = request.POST.get('contact')
            db_instance.account_type = request.POST.get('account_type')
            db_instance.pancard_no = request.POST.get('pancard_no')
            db_instance.save()
            return render(request, "redirect.html", locals())


# Transaction Functionalities
@login_required(login_url="/bm/")
def add_transaction(request):
    """
    adding the customer_details in customer table
    """
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
            account = request.POST.get('account_no')
            result_addtransaction = Account.objects.filter(account_no=account)
            context = {
                "result_addtransaction": result_addtransaction,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        if sub_user == 1:
            var = 1
            addtrans = Account.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            bank_data = Bank.objects.values_list('ifsc_code', flat=True).filter(ifsc_code__in=banks)
            addtrans = Account.objects.filter(bank_id__in=bank_data)
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def search_transaction(request):
    """
    defined for searching a transaction details
    """
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
    if request.method == "POST":
            account = request.POST.get('account_no')
            transaction_table = Transaction.objects.filter(account_id=account)
            context = {
                "transaction_table": transaction_table,
                "username": username
            }
            return render(request, "dashboard.html", context)
    else:
        if sub_user == 1:
            var = 1
            trans = Account.objects.all()
        else:
            banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
            bank_data = Bank.objects.values_list('ifsc_code', flat=True).filter(ifsc_code__in=banks)
            trans = Account.objects.filter(bank_id__in=bank_data)
    return render(request, "dashboard.html", locals())


@login_required(login_url="/bm/")
def update_transaction(request):
    """
    defined for updating edited details
    """
    if request.method == "POST":
            home = request.POST.get('transaction_id')
            db_instance = Transaction()
            db_instance.transaction_id = request.POST.get('transaction_id')
            db_instance.customer_id = request.POST.get('customer')
            db_instance.bank_id = request.POST.get('bank')
            db_instance.account_id = request.POST.get('account')
            db_instance.date = request.POST.get('date')
            db_instance.time = request.POST.get('time')
            db_instance.amount = request.POST.get('amount')
            db_instance.transaction_type = request.POST.get('transaction_type')
            db_instance.save()
            print ("Succesfully Saved")
            return render(request, "redirect.html", locals())


@login_required(login_url="/bm/")
def transaction_list(request):
    """
    defined for viewing Transactionlist
    """
    username = request.user.get_username()
    user = User.objects.values_list('id', flat=True).filter(username=username)
    sub_user = user[0]
    var = None
    if sub_user == 1:
        var = 1
        transaction_table = Transaction.objects.all()
    else:
        banks = UserPermission.objects.values_list('branch_id', flat=True).filter(user_id=sub_user)
        transaction_table = Transaction.objects.filter(bank_id__in=banks)
        context = {
            "transaction_table": transaction_table, 'username': username
        }
    return render(request, "dashboard.html", locals())
