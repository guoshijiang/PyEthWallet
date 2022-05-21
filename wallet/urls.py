from django.urls import path
from wallet.views import create_addr, transfer, get_balance


urlpatterns = [
    path(r"create_addr", create_addr, name="create_addr"),
    path(r"get_balance", get_balance, name="get_balance"),
    path(r"transfer", transfer, name="transfer"),
]