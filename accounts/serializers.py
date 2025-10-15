from rest_framework import serializers
from accounts.models import CustomUser, Student, Staff, Mentor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'department', 'year_of_study', 'points']

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'user', 'position', 'department']

class MentorSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    staff = StaffSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = ['id', 'staff', 'student', 'status', 'created_at', 'updated_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.get('role')
        user = CustomUser.objects.create_user(
            username = validated_data(['username']),
            email = validated_data(['email']),
            password = validated_data(['password']),
            role = role
        )