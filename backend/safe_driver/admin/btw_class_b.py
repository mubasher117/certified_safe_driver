from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from ..admin_inlines.inlines_btw_class_b import btw_inlines
from ..models.btw_class_b import *


@admin.register(BTWClassB)
class BTWClassBAdmin(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = btw_inlines

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
