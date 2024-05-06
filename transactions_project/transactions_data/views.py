import csv
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

#File upload API
@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES['sample_transactions']:
        file = request.FILES['sample_transactions']
        columns = ['TransactionID', 'CustomerName', 'TransactionDate', 'Amount', 'Status', 'InvoiceURL']

        try:
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                transaction = Transaction(
                    transaction_id=row[columns[0]],
                    customer_name=row[columns[1]],
                    transaction_date=datetime.strptime(row[columns[2]], '%Y-%m-%d').date(),
                    amount=row[columns[3]],
                    status=row[columns[4]],
                    invoice_url=row[columns[5]]
                )
                transaction.save()
            return Response({'message': 'File uploaded successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    else:
        return Response({'error': 'No file uploaded'}, status=400)

    
# Transactions API(UPDATE,DELETE , GET ALL transactions)
@api_view(['GET'])
def get_all_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_transaction(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    serializer = TransactionSerializer(instance=transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    transaction.delete()
    return Response({'message': 'Transaction deleted successfully'})
