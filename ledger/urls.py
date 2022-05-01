from django.urls import path
from . import views
urlpatterns = [
    path('', views.TransacListView.as_view(), name='ledger'),
    path('add_transaction/', views.AddTransaction.as_view(), name='add_transaction'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('income/', views.incomeView, name='income'),
    path('expense/', views.expenseView, name='expense'),
    path('api/', views.TransactionListView.as_view(), name='api'),
]
