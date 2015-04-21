from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from .models import Answer

class WriteOnly(BasePermission):
    """
    The is write-only request.
    """

    def has_permission(self, request, view):
        WRITE_METHODS = ["POST", ]
        return (
            request.method in WRITE_METHODS,
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer

class AnswerView(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (WriteOnly,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
