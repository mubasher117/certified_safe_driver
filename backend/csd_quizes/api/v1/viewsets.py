from rest_framework.viewsets import *
from .serializers import *


class ExamViewSets(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
