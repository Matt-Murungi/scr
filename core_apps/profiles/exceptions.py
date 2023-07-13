from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class CantFollowYourself(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _("You can not follow yourself")
    default_code = "forbidden"
