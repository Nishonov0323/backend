import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, LeaveRequest, Payment, Subject
from .serializers import StudentSerializer, TeacherSerializer, LeaveRequestSerializer, PaymentSerializer

logger = logging.getLogger(__name__)


class StudentRegisterView(APIView):
    def post(self, request):
        try:
            subject_name = request.data.get('subject')
            logger.debug(f"Student register request: {request.data}")
            if not subject_name:
                return Response({'error': 'Subject is required'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                subject = Subject.objects.get(name=subject_name)
                request.data['subject'] = subject.id
                serializer = StudentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"Student registered: {serializer.data}")
                    return Response({'message': 'Student registered'}, status=status.HTTP_201_CREATED)
                logger.error(f"Student serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Subject.DoesNotExist:
                logger.error(f"Subject not found: {subject_name}")
                return Response({'error': 'Subject not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"Error in StudentRegisterView: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherRegisterView(APIView):
    def post(self, request):
        try:
            subject_name = request.data.get('subject')
            logger.debug(f"Teacher register request: {request.data}")
            if not subject_name:
                return Response({'error': 'Subject is required'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                subject = Subject.objects.get(name=subject_name)
                request.data['subject'] = subject.id
                serializer = TeacherSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"Teacher registered: {serializer.data}")
                    return Response({'message': 'Teacher registered'}, status=status.HTTP_201_CREATED)
                logger.error(f"Teacher serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Subject.DoesNotExist:
                logger.error(f"Subject not found: {subject_name}")
                return Response({'error': 'Subject not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"Error in TeacherRegisterView: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeaveRequestView(APIView):
    def post(self, request):
        try:
            student_phone = request.data.get('student_phone')
            logger.debug(f"Leave request: {request.data}")
            if not student_phone:
                return Response({'error': 'Student phone is required'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                student = Student.objects.get(phone=student_phone)
                request.data['student'] = student.id
                serializer = LeaveRequestSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"Leave request submitted: {serializer.data}")
                    return Response({'message': 'Leave request submitted'}, status=status.HTTP_201_CREATED)
                logger.error(f"Leave serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                logger.error(f"Student not found: {student_phone}")
                return Response({'error': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"Error in LeaveRequestView: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentSubmitView(APIView):
    def post(self, request):
        try:
            student_phone = request.data.get('student_phone')
            logger.debug(f"Payment request: {request.data}")
            if not student_phone:
                return Response({'error': 'Student phone is required'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                student = Student.objects.get(phone=student_phone)
                request.data['student'] = student.id
                request.data['amount'] = 0
                serializer = PaymentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info(f"Payment submitted: {serializer.data}")
                    return Response({'message': 'Payment submitted'}, status=status.HTTP_201_CREATED)
                logger.error(f"Payment serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                logger.error(f"Student not found: {student_phone}")
                return Response({'error': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"Error in PaymentSubmitView: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
