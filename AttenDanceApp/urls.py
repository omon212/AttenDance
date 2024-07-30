from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AttenDanceAdd.as_view(), name='Attendance Add'),
    path('<int:year>/<int:month>/', AttenDanceAllData.as_view(), name='AttenDance year month all data'),
    path('update/<int:id>/', AttenDanceUpdate.as_view(), name='AttenDance update'),
]
