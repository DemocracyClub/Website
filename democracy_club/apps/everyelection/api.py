from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import AuthorityElectionPosition

# Serializers define the API representation.
class AuthorityElectionPosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorityElectionPosition
        fields = (
            'authority_election',
            'authority_election__election_date',
            'area',
            'seats',
        )

# ViewSets define the view behavior.
class AuthorityPositionSet(viewsets.ModelViewSet):
    queryset = AuthorityElectionPosition.objects.all()
    serializer_class = AuthorityElectionPosSerializer


