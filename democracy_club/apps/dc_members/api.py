from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from .models import Member

class WriteOnly(BasePermission):
    """
    The is write-only request.
    """

    def has_permission(self, request, view):
        WRITE_METHODS = ["POST", ]
        return (
            request.method in WRITE_METHODS
        )


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'email', 'source')

class MemberView(viewsets.ModelViewSet):
    permission_classes = (WriteOnly,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
