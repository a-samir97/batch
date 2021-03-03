from rest_framework.generics import ListCreateAPIView
from .models import Batch
from .serializers import BatchSerializer

class ListBatchesAPI(ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer