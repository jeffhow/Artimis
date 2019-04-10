from django.urls import path
from . import views

urlpatterns = [
    # path('update-lessonplan', views.update_lessonplan, name='update_lessonplan'),
    
    # Landing Page
    path('', views.index, name='index'),
    
    path('lesson-plan/<int:pk>/', views.LessonPlanView.as_view(), name='lesson-plan-detail'),
    path('lesson-plan/create/', views.LessonPlanCreate.as_view(), name='lesson-plan-create'),
    path('lesson-plan/<int:pk>/update/', views.LessonPlanUpdate.as_view(), name='lesson-plan-update'),
    path('course/create', views.CourseCreate.as_view(), name='course-create'),
]