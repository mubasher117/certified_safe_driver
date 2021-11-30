from django.contrib import admin
from django.db import models


def model_fields_possible_points(instance, fields, max_value=5):
    total = 0
    for field in fields:
        field_type = field.get_internal_type()
        if field_type == 'IntegerField':
            field_value = field.value_from_object(instance)
            if field_value > 0:
                total += max_value
    return total


def model_fields_received_points(instance, fields):
    total = 0
    for field in fields:
        field_type = field.get_internal_type()
        if field_type == 'IntegerField':
            field_value = field.value_from_object(instance)
            if field_value > 0:
                total += field_value
    return total


class BTWClassMixin:
    # @property
    def _possible_points(self):
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    # @property
    def _points_received(self):
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    # @property
    def _percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    possible_points = property(_possible_points)
    points_received = property(_points_received)
    percent_effective = property(_percent_effective)


class PreTripClassMixin:
    # @property
    def _possible_points(self):
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    # @property
    def _points_received(self):
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    # @property
    def _percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    possible_points = property(_possible_points)
    points_received = property(_points_received)
    percent_effective = property(_percent_effective)


class VRTPointMixin:
    @property
    def possible_points(self):
        if self.score > 0:
            return 4
        return 0

    @property
    def points_received(self):
        if self.score > 0:
            return self.score
        return 0

    # possible_points = property(_possible_points)
    # points_received = property(_points_received)


class BTWClassManager(models.Manager):
    # @property
    def _possible_points(self):
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    # @property
    def _points_received(self):
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    # @property
    def _percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    possible_points = property(_possible_points)
    points_received = property(_points_received)
    percent_effective = property(_percent_effective)


class DeleteAllMixin:
    actions = ['delete_all_data']

    def delete_all_data(self, request, queryset):
        queryset.delete()

    delete_all_data.short_description = 'Delete All Data'
    delete_all_data.acts_on_all = True
