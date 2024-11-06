from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, CharField, ModelSerializer

from training_site_app.models import Course, Lesson, Educator, Student

UserModel = get_user_model()


class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['pk', 'name', 'description']


class LessonSerializer(HyperlinkedModelSerializer):
    course = HyperlinkedRelatedField(
        view_name='training_site_app:course-detail',
        lookup_field='pk',
        many=False,
        queryset=Course.objects.all(),
    )

    class Meta:
        model = Lesson
        fields = ['pk', 'number', 'name', 'video', 'text', 'course', ]


class EducatorSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        view_name='training_site_app:user-detail',
        lookup_field='pk',
        many=False,
        queryset=UserModel.objects.all()
    )

    studying_on_courses = HyperlinkedRelatedField(
        view_name='training_site_app:course-detail',
        lookup_field='pk',
        many=True,
        queryset=Course.objects.all()
    )

    class Meta:
        model = Educator
        fields = ['user', 'teaches_courses']


class StudentSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        view_name='training_site_app:user-detail',
        lookup_field='pk',
        many=False,
        queryset=UserModel.objects.all()
    )

    studying_on_courses = HyperlinkedRelatedField(
        view_name='training_site_app:course-detail',
        lookup_field='pk',
        many=True,
        queryset=Course.objects.all()
    )

    class Meta:
        model = Student
        fields = ['user', 'studying_on_courses']


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username']


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
