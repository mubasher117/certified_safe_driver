from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# from safe_driver.models import TypeOfTrainingCompleted, ReasonForTraining
from safe_driver.models import SafeDriveNote, SafeDriveProd, SafeDriveEye, SafeDriveBTW, SafeDriveSWP, SafeDrivePreTrip, \
    StudentInfo

User = get_user_model()


@receiver(post_save, sender=User)
def create_initial_student_fields(sender, instance, created, **kwargs):
    if created:
        print(instance.email)
        # try:
        #     instance.student_info
        # except StudentInfo.DoesNotExist:
        #     StudentInfo.objects.create(student=instance)
