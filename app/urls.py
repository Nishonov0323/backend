from django.urls import path
from .views import StudentRegisterView, TeacherRegisterView, LeaveRequestView, PaymentSubmitView

urlpatterns = [
    path('student/register/', StudentRegisterView.as_view(), name='student_register'),
    path('teacher/register/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('leave/request/', LeaveRequestView.as_view(), name='leave_request'),
    path('payment/submit/', PaymentSubmitView.as_view(), name='payment_submit'),
]