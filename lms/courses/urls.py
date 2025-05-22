from django.urls import path

from.import views

urlpatterns=[

    path('courses-list/',views.CoursesListView.as_view(),name='courses-list'),

    path('home/',views.HomeView.as_view(),name='home'),

    path('instructor-course-list/',views.InstructorCourseListView.as_view(),name='instructor-course-list'),

    path('create-course/',views.CourseCreateView.as_view(),name='create-course'),

    path('instructor-course-detail/<str:uuid>/',views.InstructorCourseDetailView.as_view(),name='instructor-course-detail'),

    path('instructor-course-delete/<str:uuid>/',views.InstructorCourseDeleteView.as_view(),name='instructor-course-delete'),

    path('instructor-course-update/<str:uuid>/',views.InstructorCourseupdateView.as_view(),name='instructor-course-update'),





]