from django.urls import path
from .views import *

urlpatterns = [
    path('group/groups/', AllGroupView.as_view(), name='All groups'),
    path('group/<int:id>/', GroupView.as_view(), name='Group'),
    path('group/update/<int:id>/', GroupUpdateView.as_view(), name='Update Group'),
    path('group/delete/<int:id>/', GroupDeleteView.as_view(), name='Delete Group'),
    # path('group/student/add/', GroupStudentAdd.as_view(), name='Add Group'),
    # path('group/student/remove/', GroupStudentRemove.as_view(), name='Remove Student from Group'),
]
