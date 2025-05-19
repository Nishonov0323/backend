from django.contrib import admin
from .models import Subject, Room, Group, Student, Teacher, LeaveRequest, Payment


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'teacher', 'room', 'start_date', 'weekly_classes')
    search_fields = ('name', 'subject__name', 'teacher__name')
    list_filter = ('subject', 'teacher', 'room', 'start_date')
    ordering = ('start_date',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'is_approved', 'created_at')
    search_fields = ('name', 'phone', 'subject__name')
    list_filter = ('subject', 'is_approved', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('is_approved',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'experience', 'created_at')
    search_fields = ('name', 'phone', 'subject__name')
    list_filter = ('subject', 'experience', 'created_at')
    ordering = ('-created_at',)


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'reason', 'teacher_approved', 'admin_approved', 'created_at')
    search_fields = ('student__name', 'reason')
    list_filter = ('teacher_approved', 'admin_approved', 'date', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('teacher_approved', 'admin_approved')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'is_approved', 'created_at')
    search_fields = ('student__name',)
    list_filter = ('is_approved', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('is_approved',)
