from turtle import bgcolor
import django_tables2 as tables
from .models import Transac
from wallet.models import Wallet


class TransacTable(tables.Table):
    type = tables.Column(attrs={"td": {"color": "red"}})

    class Meta:
        model = Transac
        template_name = "django_tables2/bootstrap4.html"


class WalletTable(tables.Table):
    class Meta:
        model = Wallet
        template_name = "django_tables2/bootstrap4.html"
