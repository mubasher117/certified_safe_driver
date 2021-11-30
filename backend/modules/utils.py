from django.db import models


class WithChoices(models.Case):
    def __init__(self, model, field, condition=None, then=None, **lookups):
        choices = dict(model._meta.get_field(field).flatchoices)
        whens = [models.When(**{field: k, 'then': models.Value(v)}) for k, v in choices.items()]
        return super().__init__(*whens, output_field=models.CharField())
