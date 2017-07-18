from django.conf.urls import url

from . import views


urlpatterns = [
    # Login
    url(r'^$', views.login_user, name="login"),

    # Dashboard
    url(r'^dashboard$', views.dashboard, name="dashboard"),

    # Bank Urls
    url(r'^bank_form$', views.bank_form, name="bank_form"),
    url(r'^bank_list$', views.bank_list, name="bank_list"),
    # url(r'^search_bank/$', views.search_bank, name="search_bank"),
    url(r'^edit_bank$', views.edit_bank, name="edit_bank"),
    url(r'^edit_bank1$', views.edit_bank1, name="edit_bank1"),
    url(r'^update_bank$', views.update_bank, name="update_bank"),

    # Account Urls
    url(r'^add_account$', views.add_account, name="add_account"),
    url(r'^account_list$', views.account_list, name="account_list"),
    url(r'^search_account/$', views.search_account, name="search_account"),
    url(r'^edit_account$', views.edit_account, name="edit_account"),
    url(r'^edit_account1$', views.edit_account1, name="edit_account1"),
    url(r'^update_account$', views.update_account, name="update_account"),

    # Transaction Urls
    url(r'^add_transaction$', views.add_transaction, name="add_transaction"),
    url(r'^transaction_list$', views.transaction_list, name="transaction_list"),
    url(r'^search_transaction/$', views.search_transaction, name="search_transaction"),
    url(r'^update_transaction$', views.update_transaction, name="update_transaction"),

    # Logout
    url(r'^logout$', views.logout_user, name="logout"),
]
