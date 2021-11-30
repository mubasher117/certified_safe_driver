from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, authentication, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .test_quiz_serializers import *
from csd_quizes.models import *


class StudentTestExams(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]
    serializer_class = StudentTestExamSerializerByTest
    queryset = StudentTestExam.objects.all()

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return StudentTestExam.objects.filter(test_id=test_id)

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs['test_id'])


class StudentTestExamDetail(RetrieveUpdateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StudentTestExamSerializerByTest
    queryset = StudentTestExam.objects.all()

    def get_object(self):
        try:
            obj = get_object_or_404(self.get_queryset(), exam_id=self.kwargs['exam_id'], test_id=self.kwargs['test_id'])
            # obj = StudentTestExam.objects.get(exam_id=self.kwargs['exam_id'], test_id=self.kwargs['test_id'])
            # obj = StudentTestExam.objects.get(id=self.kwargs['exam_id'])
            return obj
        except StudentTestExam.DoesNotExist:
            return Http404

    # def get_queryset(self):
    #     test_id = self.kwargs['test_id']
    #     return StudentTestExam.objects.filter(test_id=test_id)


class TestExamSubmitAnswers(APIView):
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request, *args, **kwargs):
        exam_id = kwargs['exam_id']
        test_id = kwargs['test_id']

        items = request.data
        test_exam = StudentTestExam.objects.get(test_id=test_id, exam_id=exam_id)
        new_items = [item.update({'test_exam': test_exam.id}) for item in items]
        total_questions = test_exam.exam.total_questions
        if total_questions != len(request.data):
            return Response({
                'error': 'Submit all the question answers',
            }, status=400)
        serializer = QuestionAnswerSubmitSerializer(data=request.data, many=True)
        # if test_exam.answer_student_test_exam.count() > 0:
        #     serializer =
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TestExamAnswerList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        exam_id = kwargs['exam_id']
        test_id = kwargs['test_id']
        answers = None
        questions = None
        data = {
            'exam': None,
            # 'questions': None,
            'total_answers': 0,
            'total_correct_answers': 0,
            'total_questions': 0,
            'percentage': 0,
            'answers': None,
        }
        try:
            test_exam = StudentTestExam.objects.select_related('exam').prefetch_related(
                'answer_student_test_exam',
            ).get(test_id=test_id, exam_id=exam_id)
        except StudentTestExam.DoesNotExist:
            test_exam = None
            return Response({'detail': 'No Exam found'}, status=status.HTTP_404_NOT_FOUND)

        if test_exam:
            data['exam'] = StudentTestExamSerializerByTest(test_exam).data
            answers = test_exam.answer_student_test_exam.select_related('question', 'test_exam').prefetch_related(
                'answers', 'question__correct_choices', 'question__choices'
            ).all()
            questions = test_exam.exam.exam_questions.all()
            total_questions = questions.count()
            total_answers = answers.count()
            data['total_questions'] = total_questions
            data['total_answers'] = total_answers

        # if questions and questions.count() > 0:
        #     serializer = QuestionSerializer(questions, many=True)
        #     data['questions'] = serializer.data

        if answers and answers.count() > 0:
            serializer = QuestionAnswerReadSerializer(answers, many=True)
            data['answers'] = serializer.data
            total_correct_answers = len([x for x in data['answers'] if x['check_answer']])
            data['total_correct_answers'] = total_correct_answers
            if data['total_questions'] >= data['total_correct_answers']:
                percentage = (100 / data['total_questions']) * data['total_correct_answers']
                data['percentage'] = "{:.2f}".format(percentage)
            return Response(data)

        return Response({'error': 'No answer for this Test Exam'}, status=400)


# defensive_driving
class StudentTestDefensiveDrivingExamDetail(RetrieveUpdateAPIView):
    serializer_class = StudentTestExamSerializerByTest
    queryset = StudentTestExam.objects.all()

    def get_object(self):
        try:
            exam = Exam.objects.get(exam_type='defensive_driving')
        except Exam.DoesNotExist:
            exam = Exam.objects.create(exam_type='defensive_driving', title='Defensive Driving Quiz')

        if exam:
            try:
                obj = StudentTestExam.objects.get(exam=exam, test_id=self.kwargs['test_id'])
                return obj
            except StudentTestExam.DoesNotExist:
                obj = StudentTestExam.objects.create(test_id=self.kwargs.get('test_id'), exam=exam)
                return obj
            except Exception as e:
                print(e)
                return Http404
        return Http404


class DefensiveDrivingExamSubmitAnswers(APIView):
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request, *args, **kwargs):
        test_id = kwargs['test_id']
        items = request.data
        exam = Exam.objects.get(exam_type='defensive_driving')
        try:
            test_exam = StudentTestExam.objects.get(test_id=test_id, exam=exam)
        except StudentTestExam.DoesNotExist:
            test_exam = StudentTestExam.objects.create(test_id=test_id, exam=exam)

        new_items = [item.update({'test_exam': test_exam.id}) for item in items]
        total_questions = test_exam.exam.total_questions
        if total_questions != len(request.data):
            return Response({
                'error': 'Submit all the question answers',
            }, status=400)
        serializer = QuestionAnswerSubmitSerializer(data=request.data, many=True)
        # if test_exam.answer_student_test_exam.count() > 0:
        #     serializer =
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DefensiveDrivingExamAnswerList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        test_id = kwargs['test_id']
        exam = Exam.objects.get(exam_type='defensive_driving')
        answers = None
        questions = None
        data = {
            'exam': None,
            # 'questions': None,
            'total_answers': 0,
            'total_correct_answers': 0,
            'total_questions': 0,
            'percentage': 0,
            'answers': None,
        }
        try:
            test_exam = StudentTestExam.objects.select_related('exam',).prefetch_related(
                'answer_student_test_exam', 'exam__exam_questions',
            ).get(test_id=test_id, exam=exam)
        except StudentTestExam.DoesNotExist:
            test_exam = None
            return Response({'detail': 'No Exam found'}, status=status.HTTP_404_NOT_FOUND)

        if test_exam:
            data['exam'] = StudentTestExamSerializerByTest(test_exam).data
            answers = QuestionAnswer.objects.filter(test_exam=test_exam).select_related('question', 'test_exam') \
                .prefetch_related('answers', 'question__correct_choices', 'question__choices', 'question__choice_question'
                                  ).all()
            questions = test_exam.exam.exam_questions.all()
            total_questions = questions.count()
            total_answers = answers.count()
            data['total_questions'] = total_questions
            data['total_answers'] = total_answers

        # if questions and questions.count() > 0:
        #     serializer = QuestionSerializer(questions, many=True)
        #     data['questions'] = serializer.data

        if answers and answers.count() > 0:
            serializer = QuestionAnswerReadSerializer(answers, many=True)
            data['answers'] = serializer.data
            total_correct_answers = len([x for x in data['answers'] if x['check_answer']])
            data['total_correct_answers'] = total_correct_answers
            if data['total_questions'] >= data['total_correct_answers']:
                percentage = (100 / data['total_questions']) * data['total_correct_answers']
                data['percentage'] = "{:.2f}".format(percentage)
            return Response(data)

        return Response({'error': 'No answer for this Test Exam'}, status=400)


# distracted
class StudentTestDistractedExamDetail(RetrieveUpdateAPIView):
    serializer_class = StudentTestExamSerializerByTest
    queryset = StudentTestExam.objects.all()

    def get_object(self):
        try:
            exam = Exam.objects.get(exam_type='distracted')
        except Exam.DoesNotExist:
            exam = Exam.objects.create(exam_type='distracted', title='Distracted Quiz')

        if exam:
            try:
                obj = StudentTestExam.objects.get(exam=exam, test_id=self.kwargs['test_id'])
                return obj
            except StudentTestExam.DoesNotExist:
                obj = StudentTestExam.objects.create(test_id=self.kwargs.get('test_id'), exam=exam)
                return obj
            except Exception as e:
                print(e)
                return Http404
        return Http404


class DistractedExamSubmitAnswers(APIView):
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request, *args, **kwargs):
        test_id = kwargs['test_id']
        items = request.data
        exam = Exam.objects.get(exam_type='distracted')
        try:
            test_exam = StudentTestExam.objects.get(test_id=test_id, exam=exam)
        except StudentTestExam.DoesNotExist:
            test_exam = StudentTestExam.objects.create(test_id=test_id, exam=exam)

        new_items = [item.update({'test_exam': test_exam.id}) for item in items]
        total_questions = test_exam.exam.total_questions
        if total_questions != len(request.data):
            return Response({
                'error': 'Submit all the question answers',
            }, status=400)
        serializer = QuestionAnswerSubmitSerializer(data=request.data, many=True)
        # if test_exam.answer_student_test_exam.count() > 0:
        #     serializer =
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DistractedExamAnswerList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        test_id = kwargs['test_id']
        exam = Exam.objects.get(exam_type='distracted')
        answers = None
        questions = None
        data = {
            'exam': None,
            # 'questions': None,
            'total_answers': 0,
            'total_correct_answers': 0,
            'total_questions': 0,
            'percentage': 0,
            'answers': None,
        }
        try:
            test_exam = StudentTestExam.objects.select_related('exam').prefetch_related(
                'answer_student_test_exam',
            ).get(test_id=test_id, exam=exam)
        except StudentTestExam.DoesNotExist:
            test_exam = None
            return Response({'detail': 'No Exam found'}, status=status.HTTP_404_NOT_FOUND)

        if test_exam:
            data['exam'] = StudentTestExamSerializerByTest(test_exam).data
            answers = test_exam.answer_student_test_exam.select_related('question', 'test_exam').prefetch_related(
                'answers', 'question__correct_choices', 'question__choices'
            ).all()
            questions = test_exam.exam.exam_questions.all()
            total_questions = questions.count()
            total_answers = answers.count()
            data['total_questions'] = total_questions
            data['total_answers'] = total_answers

        if answers and answers.count() > 0:
            serializer = QuestionAnswerReadSerializer(answers, many=True)
            data['answers'] = serializer.data
            total_correct_answers = len([x for x in data['answers'] if x['check_answer']])
            data['total_correct_answers'] = total_correct_answers
            if data['total_questions'] >= data['total_correct_answers']:
                percentage = (100 / data['total_questions']) * data['total_correct_answers']
                data['percentage'] = "{:.2f}".format(percentage)
            return Response(data)

        return Response({'error': 'No answer for this Test Exam'}, status=400)
