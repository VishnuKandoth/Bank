# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Login(models.Model):
    """
    Create a Login table in database
    """
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)


class Bank(models.Model):
    """
    create a Bank table in database
    """
    branch_name = models.CharField(max_length=30, null=False)
    ifsc_code = models.CharField(max_length=25, primary_key=True)
    address = models.CharField(max_length=200)
    contact_no = models.BigIntegerField(default=None)

    def __str__(self):
        """
        defined for primary key
        """
        return self.ifsc_code


class Account(models.Model):
    """
    create a Account table in database
    """
    account_no = models.BigIntegerField(primary_key=True)
    account_holder = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField(default=None)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=30)
    pancard_no = models.CharField(max_length=30)

    def __unicode__(self):
        """
        defined for primary key
        """
        return unicode(self.account_no)


Transaction_Choices = [('Debit', 'Debit'), ('Credit', 'Credit')]


class Transaction(models.Model):
    """
    create a Transaction table in database
    """
    transaction_id = models.BigIntegerField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    amount = models.IntegerField(default=None)
    transaction_type = models.CharField(max_length=10, choices=Transaction_Choices)

    def __unicode__(self):
        """
        defined for primary key
        """
        return unicode(self.transaction_id)


class UserPermission(models.Model):
    """
    Model created for user permission
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Bank, on_delete=models.CASCADE)
