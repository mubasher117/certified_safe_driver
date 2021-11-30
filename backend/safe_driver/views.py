from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from io import BytesIO
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from xhtml2pdf import pisa

# Create your views here.
from django.views.generic import DetailView
from .models import *


class StudentProdReportPreview(DetailView):
    model = SafeDriveProd
    template_name = 'reports/prod.html'
    context_object_name = 'prod'

    def get_object(self, queryset=None):
        return SafeDriveProd.objects.get(student_id=self.kwargs['student_id'])


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def prod_report_download(request, student_id):
    obj = SafeDriveProd.objects.get(student_id=student_id)
    data = {
        "prod": obj
    }
    pdf = render_to_pdf('reports/prod.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
    # return HttpResponse(obj.id)


def accident_probability_graph_btw_class_a(request, student_id, test_id, class_name):
    data = {
        'student_id': student_id,
        'test_id': test_id,
        'class_name': class_name,
    }
    return render(request, 'btw/class_a_accident_probability_graph.html', data)


