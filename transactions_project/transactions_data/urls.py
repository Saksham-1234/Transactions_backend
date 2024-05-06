
from django.urls import path
from .views import upload_file, get_all_transactions, update_transaction, delete_transaction

urlpatterns = [
    path('upload/', upload_file, name='upload-file'),
    path('', get_all_transactions, name='all-transactions'),
    path('<str:transaction_id>/', update_transaction, name='update-transaction'),
    path('<str:transaction_id>/delete/', delete_transaction, name='delete-transaction'),

]
