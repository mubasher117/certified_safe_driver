from openpyxl.cell import read_only
from rest_framework import serializers

from safe_driver.api.v1.serializers import StudentTestSerializer
from truck_driving_school.models import *


class DefensiveDriverKnowledgeQuizSerializer(serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)

    class Meta:
        model = DefensiveDriverKnowledgeQuiz
        fields = '__all__'


# class TrainingLocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TrainingLocation
#         fields = '__all__'


class TrainingRecordCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingRecordComment
        fields = '__all__'
        extra_kwargs = {
            'training_record': {
                'read_only': True
            }
        }

    # def create(self, validated_data):
    #     training_record = validated_data.get('training_record')
    #     print(training_record)
    #     # return super(TrainingRecordDayCommentSerializer, self).create(validated_data)
    #     return validated_data


class DriverTrainigRecordSerializer(serializers.ModelSerializer):
    day = serializers.IntegerField(required=True)
    location = serializers.ChoiceField(choices=TRAINING_LOCATION_CHOICES, required=True)
    location_name = serializers.CharField(read_only=True)
    comment = TrainingRecordCommentSerializer(required=False, allow_null=True)

    class Meta:
        model = DriverTrainigRecord
        fields = '__all__'

        extra_kwargs = {
            'test': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        if 'comment' in attrs:
            if attrs.get('comment') is None or attrs.get('comment') == 'null' or attrs.get('comment') == "":
                attrs.pop('comment')
        return attrs

    def update(self, instance, validated_data):
        comment = None
        if 'comment' in validated_data:
            comment = validated_data.pop('comment')
        super(DriverTrainigRecordSerializer, self).update(instance, validated_data)
        if comment:
            try:
                comment_instance = instance.comment
                comment_serializer = TrainingRecordCommentSerializer().update(comment_instance, comment)
            except TrainingRecordComment.DoesNotExist:
                TrainingRecordComment.objects.create(training_record=instance, **comment)

        return instance


class SchoolHoursSerializer(serializers.ModelSerializer):
    driver_trainer_signature = serializers.CharField(required=False, write_only=True)
    total_days = serializers.IntegerField(read_only=True)

    class Meta:
        model = SchoolHours
        fields = '__all__'

        extra_kwargs = {
            'test': {
                'read_only': True
            }
        }

    def to_representation(self, instance):
        res = super(SchoolHoursSerializer, self).to_representation(instance)
        if instance.driver_trainer_signature:
            res['driver_trainer_signature'] = instance.driver_trainer_signature.url
        else:
            res['driver_trainer_signature'] = None

        return res

    def update(self, instance, validated_data):
        from safe_driver.image_functions import base64_to_image_content
        if 'driver_trainer_signature' in validated_data:
            driver_trainer_signature = validated_data.pop('driver_trainer_signature')
            try:
                image_content_file = base64_to_image_content(driver_trainer_signature)
                validated_data['driver_trainer_signature'] = image_content_file
            except:
                pass

        return super(self.__class__, self).update(instance, validated_data)


class DQFRequirementItemSerializer(serializers.ModelSerializer):
    department_display_name = serializers.CharField(read_only=True)

    class Meta:
        model = DQFRequirementItem
        fields = '__all__'


class SchoolControlDQFRequirementSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        res = super(SchoolControlDQFRequirementSerializer, self).to_representation(instance)
        try:
            res['item'] = DQFRequirementItemSerializer(instance.item).data
        except Exception as e:
            print(e)
            res['item'] = None

        return res

    class Meta:
        model = SchoolControlDQFRequirement
        fields = '__all__'
        extra_kwargs = {
            'test': {
                'read_only': True
            }
        }


class TraneeBookItemSerializer(serializers.ModelSerializer):
    department_display_name = serializers.CharField(read_only=True)

    class Meta:
        model = TraineeBookItem
        fields = '__all__'


class TraneeBookSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        res = super(TraneeBookSerializer, self).to_representation(instance)
        try:
            res['item'] = TraneeBookItemSerializer(instance.item).data
        except:
            res['item'] = None

        return res

    class Meta:
        model = TraineeBook
        fields = '__all__'

        extra_kwargs = {
            'test': {
                'read_only': True
            }
        }


class TrainginRecordDayCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingRecordDayComment
        fields = '__all__'

        extra_kwargs = {
            'test': {
                'read_only': True
            }
        }

    # def validate_day(self, day):
    #     validated_data = self.validate()
    #     print(validated_data)
    #     return day

    def create(self, validated_data):
        test = validated_data.get('test_id')
        day = validated_data.get('day')

        day_comment = TrainingRecordDayComment.objects.filter(test_id=test, day=day)
        if day_comment.exists():
            raise serializers.ValidationError(
                {
                    'day': 'Day %s: Comment already exist' % day
                }
            )

        print(test)
        return super(TrainginRecordDayCommentSerializer, self).create(validated_data)
