from rest_framework import serializers
from discipline.models import DisciplineReport

class DisciplineReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineReport
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']