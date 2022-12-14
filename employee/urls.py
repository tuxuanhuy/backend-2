from django.urls import path, include

from .views import *

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employee/<int:pk>/shift', EmployeeShift.as_view(), name='employee_detail'),

    path('shift/', ShiftList.as_view(), name='shift_list'),
    path('shift/search/', ShiftSearch.as_view(), name='shift_search'),
    path('shift/<int:pk>/', ShiftDetail.as_view(), name='shift_detail'),


	# path('employee/', views.employee_list, name='employee_list'),
	# path('employee/<int:pk>/', views.employee_detail, name="employee_detail"),
	# path('employee/<int:pk>/edit/', views.employee_update, name="employee_update"),

    # path('employee/add', views.employee_add, name="employee_add"),

]
