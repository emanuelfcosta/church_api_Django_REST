from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from church.models import Member, Church, Financial, Occasion, Prayer, Study
from .serializer import (
    MemberSerializer,
    ChurchSerializer,
    FinancialSerializer,
    OccasionSerializer,
    PrayerSerializer,
    StudySerializer
)
class MembersViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ChurchViewSet(viewsets.ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        church = self.get_object()
        members = church.members.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)


class FinancialViewSet(viewsets.ModelViewSet):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer


class OccasionViewSet(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer


class PrayerViewSet(viewsets.ModelViewSet):
    queryset = Prayer.objects.all()
    serializer_class = PrayerSerializer


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
