import base64
from uuid import uuid4

from django.core.files.base import ContentFile


def base64_to_image_content(image_string):
    file_format, imgstr = image_string.split(';base64,')
    ext = file_format.split('/')[-1]
    filename = '%s.%s' % (uuid4(), ext)
    image_bytes = imgstr.encode('utf-8')
    # print(imgstr)
    decoded_string = base64.decodebytes(image_bytes)
    # print(decoded_string)
    content = ContentFile(decoded_string, name=filename)
    return content


def signature_image_folder(self, filename):
    url = "test_%s/signatures/%s" % (self.test.id, filename)
    return url


def map_image_folder(self, filename):
    url = "test_%s/signatures/%s" % (self.test.id, filename)
    return url
