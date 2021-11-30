from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.views import APIView


class SerializerFiledAttributesMixin():
    def to_representation(self, instance):
        """Object instance -> Dict of primitive datatypes."""
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                value = None
            else:
                value = field.to_representation(attribute)

            ret[field.field_name] = {
                'value': value,
                # You can find more field attributes here
                # https://github.com/encode/django-rest-framework/blob/master/rest_framework/fields.py#L324
                'verbose_name': field.label,
                'read_only': field.read_only,
                'write_only': field.write_only,
                'help_text': field.help_text,
            }

        return ret


class FactorAPIView(APIView):
    @property
    def factor_data(self):
        return {
            'animal': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'backing': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'cyclist': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'entering_exiting': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hazardous_materials': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'head_on_collision': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hit_in_rear': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hit_other_in_rear': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hit_parked_vehicle': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hit_stationary_object': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'hit_while_parked': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'intersection': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'jacknife': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'moving_object': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'parking_lot': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'rollaway': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'sideswipe': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
        }


class DBTableNameMixin(serializers.Serializer):
    db_table = serializers.SerializerMethodField(read_only=True, method_name='get_db_table')

    def get_db_table(self, instance=None):
        if instance:
            return '%s' % instance._meta.db_table
        return None
