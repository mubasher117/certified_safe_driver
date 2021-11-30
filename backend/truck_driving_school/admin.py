from django.contrib import admin
from .models import *


@admin.register(DefensiveDriverKnowledgeQuiz)
class DefensiveDriverKnowledgeQuizAdmin(admin.ModelAdmin):
    list_display = ['test']


# @admin.register(TrainingLocation)
# class TrainingLocationAdmin(admin.ModelAdmin):
#     list_display = ['name', 'created', 'updated']

@admin.register(TrainingRecordCSVTemplate)
class TrainingRecordCSVTemplateAdmin(admin.ModelAdmin):
    list_display = ['company', 'created', 'updated']


@admin.register(DriverTrainigRecord)
class DriverTrainigRecordAdmin(admin.ModelAdmin):
    list_display = ['test', 'title', 'day', 'position', 'location', 'planned', 'actual', 'created', 'updated']
    list_editable = ['position', 'day']
    search_fields = ['title',  'location']


@admin.register(SchoolHours)
class SchoolHoursAdmin(admin.ModelAdmin):
    list_display = ['test', 'start_date', 'end_date', 'created', 'updated']
    autocomplete_fields = ('test',)


@admin.register(DQFRequirementItem)
class DQFRequirementItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'position', 'created', 'updated']
    search_fields = ('title', 'department',)


@admin.register(SchoolControlDQFRequirement)
class SchoolControlDQFRequirementAdmin(admin.ModelAdmin):
    list_display = ['test', 'get_item_title', 'get_item_postion', 'initials', 'date', 'created', 'updated']
    list_select_related = ('test', 'item')
    autocomplete_fields = ('test', 'item')

    def get_item_title(self, instance):
        if instance.item:
            return '%s' % instance.item.title
        return None

    def get_item_postion(self, instance):
        if instance.item:
            return '%s' % instance.item.position
        return None

    get_item_title.short_description = 'Title'
    get_item_postion.short_description = 'Position'
    get_item_postion.admin_order_field = 'item__position'
    # get_dqf_requirement_title = 'dqf_requirement__title'


@admin.register(TraineeBookItem)
class TraineeBookItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'created', 'updated']
    search_fields = ('title', 'department',)


@admin.register(TraineeBook)
class TraineeBookAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'test', 'initials', 'date', 'created', 'updated']
    autocomplete_fields = ('test', 'item')

    def get_item_title(self, instance):
        if instance.item:
            return '%s' % instance.item.title
        return None

    get_item_title.short_description = 'Title'


@admin.register(TrainingRecordDayComment)
class TrainginRecordDayCommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'test', 'day', 'created', 'updated']


@admin.register(TrainingRecordComment)
class TrainingRecordCommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'body', 'created', 'updated']
    autocomplete_fields = ('training_record', )
