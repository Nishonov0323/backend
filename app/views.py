from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, LeaveRequest, Payment, Subject
from .serializers import StudentSerializer, TeacherSerializer, LeaveRequestSerializer, PaymentSerializer

class StudentRegisterView(APIView):
    def post(self, request):
        subject_name = request.data.get('subject')
        try:
            subject = Subject.objects.get(name=subject_name)
            request.data['subject'] = subject.id
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Student registered'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=status.HTTP_400_BAD_REQUEST)

class TeacherRegisterView(APIView):
    def post(self, request):
        subject_name = request.data.get('subject')
        try:
            subject = Subject.objects.get(name=subject_name)
            request.data['subject'] = subject.id
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Teacher registered'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=status.HTTP_400_BAD_REQUEST)

class LeaveRequestView(APIView):
    def post(self, request):
        student_phone = request.data.get('student_phone')
        try:
            student = Student.objects.get(phone=student_phone)
            request.data['student'] = student.id
            serializer = LeaveRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Leave request submitted'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)

class PaymentSubmitView(APIView):
    def post(self, request):
        student_phone = request.data.get('student_phone')
        try:
            student = Student.objects.get(phone=student_phone)
            request.data['student'] = student.id
            request.data['amount'] = 0
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Payment submitted'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)