from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def model_field_list(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    return field_list


def model_field_list_with_boolean(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField' or \
                            rel_field.get_internal_type() == 'BooleanField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    return field_list


def db_table_list(model):
    table_list = []
    fields = model._meta.get_fields()
    for field in fields:
        # print(model._meta.get_field(str(field.name)))
        if field.name != 'test':
            try:
                related_model = model._meta.get_field(str(field.name)).related_model

                db_table = related_model._meta.db_table
                model_name = related_model._meta.verbose_name.title()
                if related_model:
                    table_list.append(
                        (db_table, model_name)
                    )
            except:
                pass
    return table_list


def model_integer_field_names(model):
    field_list = []
    fields = model._meta.get_fields()

    for field in fields:
        try:
            related_model = model._meta.get_field(str(field.name)).related_model
            related_fields = related_model._meta.get_fields()
            if related_fields:
                for rel_field in related_fields:
                    # print(rel_field.verbose_name)
                    if rel_field.get_internal_type() == 'IntegerField':
                        field_list.append(
                            (rel_field.name, rel_field.verbose_name)
                        )
        except:
            pass
    return field_list


def model_integer_field_names_with_boolean(model):
    field_list = []
    fields = model._meta.get_fields()

    for field in fields:
        try:
            related_model = model._meta.get_field(str(field.name)).related_model
            related_fields = related_model._meta.get_fields()
            if related_fields:
                for rel_field in related_fields:
                    # print(rel_field)
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField' or \
                            rel_field.get_internal_type() == 'BooleanField':
                        field_list.append(
                            (rel_field.name, rel_field.verbose_name)
                        )
        except:
            pass
    return field_list


def html_field_data(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    # print(field_list)
    html_content = render_to_string('fields/field_list.html', {'fields': field_list})
    # print(html_content)

    return mark_safe(html_content)


def html_field_data_with_boolean(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField' or rel_field.get_internal_type() == \
                            'BooleanField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    # print(field_list)
    html_content = render_to_string('fields/field_list.html', {'fields': field_list})
    # print(html_content)

    return mark_safe(html_content)
