import json

from django.db.models import Count, Sum, Q
from django.db.models.functions import Coalesce
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from modules.utils import WithChoices
from safe_driver.models import StudentInfo
from users.api.v1.permissions import InstructorPermission
from .serializers import *
from django.core import serializers as core_serializers


class DefensiveDriverKnowledgeQuizDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = DefensiveDriverKnowledgeQuizSerializer

    queryset = DefensiveDriverKnowledgeQuiz.objects.all()

    def get_object(self):
        try:
            instance = DefensiveDriverKnowledgeQuiz.objects.select_related('test', 'test__student').get(
                test=self.kwargs['test_id'])
            return instance
        except DefensiveDriverKnowledgeQuiz.DoesNotExist:
            instance = DefensiveDriverKnowledgeQuiz.objects.create(test_id=self.kwargs['test_id'])
            return instance
        except Exception as e:
            raise Http404


class DriverTrainigRecordListView(ListAPIView, CreateAPIView):
    serializer_class = DriverTrainigRecordSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs['test_id'])

    def get_queryset(self):
        test_id = self.kwargs.get('test_id')
        qs = DriverTrainigRecord.objects.select_related('test', 'comment') \
            .filter(test_id=test_id)
        # print('queryset', qs)

        return qs

    def list(self, request, *args, **kwargs):
        from itertools import groupby
        from operator import itemgetter
        test_id = self.kwargs.get('test_id')
        from truck_driving_school.utils import create_days_from_csv_template
        test = StudentTest.objects.get(id=test_id)
        main_queryset = self.get_queryset()
        # print(main_queryset)

        if main_queryset.count() < 1:
            try:
                student_info = test.student.student_info
            except StudentInfo.DoesNotExist:
                print('no info. adding Student Info Instance')
                student_info = StudentInfo.objects.create(student_id=self.kwargs.get('student_id'))
            except Exception as e:
                print(e)
                return Response({'detail': 'Student Does not have any information'}, status=404)
                # return None
            if student_info:
                if not student_info.company:
                    return Response({'detail': 'Student Info Does not have any company'}, status=404)

                try:
                    csv_template = student_info.company.training_record_csv
                except TrainingRecordCSVTemplate.DoesNotExist:
                    return Response({
                        'detail': 'Company Doesn\'t have any CSV template uploaded for initial data. You can add new data manually'},
                        status=404)

                if csv_template and csv_template.csv_file:
                    try:
                        print('Creating intial data from Company CSV Template')
                        create_days_from_csv_template(test.student.student_info.company_id, test_id)
                    except Exception as e:
                        print(e)
                        return Response({'detail': 'Failed to create initial records from CSV template.'}, status=400)

        qs = main_queryset \
            .annotate(location_name=WithChoices(DriverTrainigRecord, 'location'), ) \
            .values('id', 'day', 'test', 'title', 'location', 'location_name', 'planned', 'actual', 'initials',
                    'position', 'comment')
        if qs.count() > 0:
            days_list = qs.values_list('day', flat=True).order_by('day').distinct()
            day_comments = test.driver_training_record_day_comments.all()
            calc_total = main_queryset.aggregate(total_planned=Coalesce(Sum('planned'), 0),
                                                 total_actual=Coalesce(Sum('actual'), 0),
                                                 classroom_total_planned=Coalesce(
                                                     Sum('planned', filter=Q(location='classroom')), 0),
                                                 on_road_total_planned=Coalesce(
                                                     Sum('planned', filter=Q(location='on_road')), 0),
                                                 yard_total_planned=Coalesce(
                                                     Sum('planned', filter=Q(location='yard')), 0),
                                                 btw_total_planned=Coalesce(
                                                     Sum('planned', filter=Q(location='btw')), 0),
                                                 classroom_total_actual=Coalesce(
                                                     Sum('actual', filter=Q(location='classroom')), 0),
                                                 on_road_total_actual=Coalesce(
                                                     Sum('actual', filter=Q(location='on_road')), 0),
                                                 yard_total_actual=Coalesce(
                                                     Sum('actual', filter=Q(location='yard')), 0),
                                                 btw_total_actual=Coalesce(
                                                     Sum('actual', filter=Q(location='btw')), 0),
                                                 )
            # print(calc_total)

            calc_qs = qs.values('day').annotate(total_planned=Coalesce(Sum('planned'), 0.00),
                                                total_actual=Coalesce(Sum('actual'), 0.00),
                                                classroom_total_planned=Coalesce(
                                                    Sum('planned', filter=Q(location='classroom')), 0),
                                                on_road_total_planned=Coalesce(
                                                    Sum('planned', filter=Q(location='on_road')), 0),
                                                yard_total_planned=Coalesce(
                                                    Sum('planned', filter=Q(location='yard')), 0),
                                                btw_total_planned=Coalesce(
                                                    Sum('planned', filter=Q(location='btw')), 0),
                                                classroom_total_actual=Coalesce(
                                                    Sum('actual', filter=Q(location='classroom')), 0),
                                                on_road_total_actual=Coalesce(
                                                    Sum('actual', filter=Q(location='on_road')), 0),
                                                yard_total_actual=Coalesce(
                                                    Sum('actual', filter=Q(location='yard')), 0),
                                                btw_total_actual=Coalesce(
                                                    Sum('actual', filter=Q(location='btw')), 0),
                                                ).order_by('day')
            # print(calc_qs)

            # items = list(qs)
            # if 'day' in request.GET and request.GET.get('day') != "":
            #     items = list(qs.filter(day=request.GET.get('day')))
            #     main_queryset.filter(day=request.GET.get('day'))
            # print(items)
            # rows = groupby(items, itemgetter('day'))
            json_items = DriverTrainigRecordSerializer(main_queryset, many=True).data
            json_rows = groupby(json_items, itemgetter('day'))
            json_days = {day: list(json_items) for day, json_items in json_rows}
            # print(response_data)
            day_comments_data = TrainginRecordDayCommentSerializer(day_comments, many=True).data
            response_data = {
                'days': days_list,
                'total': calc_total,
                'counters': list(calc_qs),
                # 'day_list': {day: list(items) for day, items in rows},
                'day_list': json_days,
                'comments': day_comments_data
            }
            return Response(response_data)

        return Response({'detail': 'No item found for this test'}, status=404)


class DriverTrainingRecordAddNewDay(APIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @staticmethod
    def post(request, *args, **kwargs):
        from truck_driving_school.utils import create_next_day_training_record, create_first_day_training_record
        test = kwargs.get('test_id')
        day = request.data.get('day')
        records = DriverTrainigRecord.objects.filter(test_id=test, day=day)
        if not records:
            if day == 1 or day == "1":
                try:
                    new_items = create_first_day_training_record(test)
                    serializer = DriverTrainigRecordSerializer(new_items, many=True)
                    return Response(serializer.data)
                except:
                    return Response({'detail': 'Failed to add new items.'}, status=400)
            else:
                try:
                    new_items = create_next_day_training_record(test, day)
                    serializer = DriverTrainigRecordSerializer(new_items, many=True)
                    return Response(serializer.data)
                except:
                    return Response({'detail': 'Failed to add new items.'}, status=400)
        return Response({'detail': 'Test has data for this day. Add new manually.'}, status=400)


class DriverTrainingRecordDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = DriverTrainigRecordSerializer

    def get_queryset(self):
        return DriverTrainigRecord.objects.filter(test_id=self.kwargs.get('test_id'))

    # def get_object(self):
    #     return


class DriverTrainingRecordCommentDetails(CreateAPIView, RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    serializer_class = TrainingRecordCommentSerializer

    def perform_create(self, serializer):
        serializer.save(training_record=self.kwargs.get('pk'))

    # def
    def get_queryset(self):
        return TrainingRecordComment.objects.filter(training_record__id=self.kwargs.get('pk'))

    def get_object(self):
        try:
            return TrainingRecordComment.objects.get(training_record__id=self.kwargs.get('pk'))
        except TrainingRecordComment.DoesNotExist:
            raise Http404

    def create(self, request, *args, **kwargs):
        try:
            training_record = DriverTrainigRecord.objects.get(id=self.kwargs.get('pk'))
        except DriverTrainigRecord.DoesNotExist:
            return Response({'detail': 'No Training Record found.'}, status=404)

        try:
            comment = training_record.comment
            serializer = TrainingRecordCommentSerializer().update(comment, request.data)
            return Response(serializer)
        except TrainingRecordComment.DoesNotExist:
            serializer = TrainingRecordCommentSerializer(training_record=training_record)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)


class DeleteDriverTrainingRecord(APIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @staticmethod
    def delete(request, *args, **kwargs):
        test = kwargs.get('test_id')
        # test_obj = StudentTest.objects.get(id=test)
        # print(test_obj)
        try:
            test_obj = StudentTest.objects.get(id=test)
        except StudentTest.DoesNotExist:
            raise Http404

        if test_obj:
            print('test ok')
            try:
                instructors = test_obj.student.student_info.company.instructors.all()
                print(instructors)
            except:
                instructors = test_obj.student.student_info.company.instructors.none()
            if request.user not in instructors or not request.user.is_superuser:
                return Response({'detail': 'Permission denied.'}, status=403)

            if 'days' in request.data and 'ids' in request.data:
                return Response({'detail': 'To delete send request for only IDs or only days'}, status=400)
            if 'days' in request.GET and request.GET.get('days') != "":
                days = list(request.GET.get('days').split(','))
                # print(days)
                items = DriverTrainigRecord.objects.filter(test_id=test, day__in=days)
                # print(items)
                if items:
                    items.delete()
                    return Response(status=204)
                return Response({'detail': 'No items found.'}, status=404)

            elif 'ids' in request.GET and request.GET.get('ids') != "":
                ids = list(request.GET.get('ids').split(','))
                items = DriverTrainigRecord.objects.filter(test_id=test, pk__in=ids)
                if items:
                    items.delete()
                    return Response(status=204)
                return Response({'detail': 'No items found.'}, status=404)

            return Response({'detail': 'No IDs and Days list in params.'}, status=400)

        return Response({'detail': 'Failed to delete.'}, status=400)


class TrainingDayCommentList(ListCreateAPIView):
    serializer_class = TrainginRecordDayCommentSerializer
    queryset = TrainingRecordDayComment.objects.none()

    def paginate_queryset(self, queryset):
        return None

    def get_queryset(self):
        return TrainingRecordDayComment.objects.filter(test_id=self.kwargs.get('test_id'))

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs.get('test_id'))

    def create(self, request, *args, **kwargs):
        test = self.kwargs.get('test_id')
        day = request.data.get('day')
        day_comment = TrainingRecordDayComment.objects.filter(test_id=test, day=day)
        if day_comment.exists():
            serializer = TrainginRecordDayCommentSerializer(instance=day_comment.first(), data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        return super(TrainingDayCommentList, self).create(request, *args, **kwargs)


class SchoolHoursDetails(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SchoolHoursSerializer

    queryset = SchoolHours.objects.all()

    def get_object(self):
        try:
            return SchoolHours.objects.get(test_id=self.kwargs.get('test_id'))
        except SchoolHours.DoesNotExist:
            return SchoolHours.objects.create(test_id=self.kwargs.get('test_id'))


class DQFRequirementListView(ListAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = DQFRequirementItemSerializer
    queryset = DQFRequirementItem.objects.all()
    pagination_class = None


class SchoolControlDQFRequirementListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    serializer_class = SchoolControlDQFRequirementSerializer

    queryset = SchoolControlDQFRequirement.objects.all()
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs.get('test_id'))

    def get_queryset(self):
        main_qs = SchoolControlDQFRequirement.objects.select_related('test', 'item').filter(
            test_id=self.kwargs.get('test_id'))

        if main_qs.count() < 1:
            # print('not found')
            dqf_list = DQFRequirementItem.objects.all()
            if dqf_list.count() > 0:
                items = []
                for dqf in dqf_list:
                    item = SchoolControlDQFRequirement(**{
                        'test_id': self.kwargs.get('test_id'),
                        'item_id': dqf.id,
                    })
                    items.append(item)

                if len(items) > 0:
                    queryset = SchoolControlDQFRequirement.objects.bulk_create(items)
                    return queryset
        return main_qs


class SchoolControlDQFRequirementDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    serializer_class = SchoolControlDQFRequirementSerializer

    def get_object(self):
        try:
            return SchoolControlDQFRequirement.objects.get(test_id=self.kwargs.get('test_id'), pk=self.kwargs.get('pk'))
        except SchoolControlDQFRequirement.DoesNotExist:
            raise Http404


class TraineeBookItemListView(ListAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = TraneeBookItemSerializer
    queryset = TraineeBookItem.objects.all()
    pagination_class = None


class TraineeBookListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    serializer_class = TraneeBookSerializer

    queryset = TraineeBook.objects.all()
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs.get('test_id'))

    def get_queryset(self):
        main_qs = TraineeBook.objects.select_related('test', 'item').filter(
            test_id=self.kwargs.get('test_id'))

        if main_qs.count() < 1:
            print('not found')
            item_list = TraineeBookItem.objects.all()
            if item_list.count() > 0:
                items = []
                for item in item_list:
                    item = TraineeBook(**{
                        'test_id': self.kwargs.get('test_id'),
                        'item_id': item.id,
                    })
                    items.append(item)

                if len(items) > 0:
                    queryset = TraineeBook.objects.bulk_create(items)
                    return queryset
        return main_qs


class TraineeBookDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    serializer_class = TraneeBookSerializer

    def get_object(self):
        try:
            return TraineeBook.objects.get(test_id=self.kwargs.get('test_id'), pk=self.kwargs.get('pk'))
        except TraineeBook.DoesNotExist:
            raise Http404
