import json

from django.contrib.auth import get_user_model
from django.db.models import Q, Count, Sum
from django.db.models.functions import TruncMonth, ExtractMonth, ExtractYear
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()


class ChartNumberOfStudentsByMonths(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        data_year = request.GET.get('year')
        if data_year and data_year != "":
            try:
                students = User.objects.filter(is_student=True).filter(date_joined__year=data_year) \
                    .annotate(month=ExtractMonth('date_joined')) \
                    .values('month') \
                    .annotate(total=Count('pk')) \
                    .order_by('month')
                # print(students)
                # students = User.objects.filter(is_student=True) \
                #     .values('date_joined__year', 'date_joined__month') \
                #     .annotate(count=Count('pk'))
                data = {
                    'year': data_year,
                    'year_total': students.aggregate(year_total=Sum('total'))['year_total'],
                    'data': list(students)
                }
                return Response(data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response(None, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Year parameter missing'}, status=status.HTTP_400_BAD_REQUEST)
