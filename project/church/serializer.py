from rest_framework import serializers

from church.models import Member, Church, Financial, Occasion, Prayer, Study

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ChurchSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Church
        fields = '__all__'


class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = '__all__'


class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = '__all__'


class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer
        fields = '__all__'


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'
