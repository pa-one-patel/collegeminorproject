from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User
from datetime import datetime,date
from datetime import timedelta
from django.utils import timezone

class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo=models.FileField()
    specialization=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})


class LeaveRequest(models.Model):
    faculty=models.ForeignKey(to=Faculty, related_name="request", null=True, blank=True)
    start=models.DateField(default=timezone.now)
    end=models.DateField(default=timezone.now)
    type=models.IntegerField(
        choices=((1,"Medical"),(2,'Casual'),(3,'Earned'),(4,'Vacation')),
        default=3,
        )
    status=models.IntegerField(
        choices=((1,"Accepted"),(2,'Rejected'),(3,'Pending')),
        default=3,
        )
    reason=models.CharField(max_length=900)
    verdict=models.CharField(max_length=900,null=True)
    def days(self):
        days = self.end-self.start + timedelta(1)
        return days



class LeaveRecord(models.Model):
    faculty=models.OneToOneField(Faculty,on_delete=models.CASCADE,null=True)
    casual_leave=models.IntegerField(default=13)
    earned_leave=models.IntegerField(default=15)
    sick_leave=models.IntegerField(default=5)
    vacation_leave=models.IntegerField(default=30)
