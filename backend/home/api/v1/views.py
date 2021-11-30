from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from safe_driver.image_functions import base64_to_image_content


@api_view(['POST'])
def base64_to_image(request):
    file_content = base64_to_image_content(request.data.get('image'))
    file_name = default_storage.save(file_content.name, file_content)
    file = default_storage.open(file_name)
    file_url = default_storage.url(file_name)

    return Response({'url': file_url})

@api_view(['GET'])
def db_url(request):
    from django.conf import settings

    return Response({'db': settings.DATABASE_URL})