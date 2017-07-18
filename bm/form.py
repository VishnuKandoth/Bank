from django import forms
from .models import Bank, Account, Transaction


class LoginForm(forms.Form):
    """
    create login form
    """
    UserID = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'Placeholder': 'UserID',
                                                                          'class': 'login_field'}))

    Password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'Placeholder': 'Password',
                                                                                'class': 'login_field'}))


class BankDetail(forms.ModelForm):
    """
    create Bank_details form according to model
    """
    class Meta:
        model = Bank
        fields = '__all__'
        widgets = {
            'bank_name': forms.TextInput(attrs={'placeholder': 'Bank Name', 'class': 'textfield'}),
            'branch_name': forms.TextInput(attrs={'placeholder': 'Branch Name', 'class': 'textfield'}),
            'ifsc_code': forms.TextInput(attrs={'placeholder': 'IFSC Code', 'class': 'textfield'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address', 'class': 'textarea'}),
            'contact_no': forms.TextInput(attrs={'placeholder': 'Contact Number', 'class': 'textfield'}),
        }


class AccountDetail(forms.ModelForm):
    """
    create Account_Detail form according to model
    """
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'account_no': forms.TextInput(attrs={'placeholder': 'Account Number', 'class': 'textfield_custname'}),

            'bank': forms.Select(attrs={'class': 'account_drop'}),

            'address': forms.Textarea(attrs={'placeholder': 'Customer Address', 'class': 'customer_textarea'}),

            'contact': forms.TextInput(attrs={'placeholder': 'Customer Contact', 'class': 'textfield_custcontact'}),

            'account_type': forms.TextInput(attrs={'placeholder': 'Account Type', 'class': 'textfield_custcontact'}),

            'pancard_no': forms.TextInput(attrs={'placeholder': 'Pancard Number', 'class': 'textfield_pancard'}), }


class TransactionDetail(forms.ModelForm):
    """
    create Transaction_Detail form according to model
    """
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'transaction_id': forms.TextInput(attrs={'placeholder': 'Transaction ID', 'class': 'transaction_text'}),

            'account': forms.Select(attrs={'class': 'account_drop'}),

            'bank': forms.Select(attrs={'class': 'transform_bankdrop'}),

            'customer': forms.Select(attrs={'class': 'customer_drop'}),

            'date': forms.DateInput(attrs={'placeholder': 'Transaction Date', 'class': 'datetime'}),

            'time': forms.TimeInput(attrs={'placeholder': 'Transaction Time', 'class': 'datetime'}),

            'amount': forms.NumberInput(attrs={'placeholder': 'Amount', 'class': 'amount'}),

            'transaction_type': forms.Select(attrs={'class': 'type_drop'}), }


class SearchBank(forms.ModelForm):
    """
    creates form for searching Bank
    """
    class Meta:
        searchlist = Bank.objects.values_list('branch_name', flat=True).distinct()
        model = Bank
        fields = ['branch_name']
        widgets = {'branch_name': forms.Select(choices=((x, x) for x in searchlist), attrs={'class': 'search_drop'})}


class SearchAccount(forms.ModelForm):
    """
    creates form for searching Account
    """
    class Meta:
        searchlist = Account.objects.values_list('account_no', flat=True).distinct()
        model = Account
        fields = ['account_type']
        widgets = {'account_type': forms.Select(choices=((x, x) for x in searchlist), attrs={'class': 'search_drop'})}


class SearchTransaction(forms.ModelForm):
    """
    creates form for searching transaction
    """
    class Meta:
        model = Transaction
        fields = ['account']
        widgets = {'account': forms.Select(attrs={'class': 'search_drop'})}


class EditBank(forms.ModelForm):
    """
    creates form for editing Bank
    """
    class Meta:
        model = Account
        fields = ['bank']
        widgets = {'bank': forms.Select(attrs={'class': 'search_drop'})}


class EditAccount(forms.ModelForm):
    """
    creates form for editing Account
    """
    class Meta:
        model = Transaction
        fields = ['account']
        widgets = {'account': forms.Select(attrs={'class': 'search_drop'})}


class AddTransaction(forms.ModelForm):
    """
    creates form for searching transaction
    """
    class Meta:
        model = Account
        fields = ['account_no']
        widgets = {'account_no': forms.Select(attrs={'class': 'search_drop'})}
