from django.db import models

class enquiryForm(models.Model):
  fullName = models.CharField(max_length=200, blank=False)
  email = models.EmailField(blank=False)
  mobile = models.IntegerField(blank=False)
  courseInterest = models.CharField(max_length=150, blank=False)
  city = models.CharField(max_length=100, blank=False)
  state = models.CharField(max_length=100, blank=False)
  zipcode = models.IntegerField(blank=False)
  dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
  claimed_by = models.CharField(max_length=50, default=None)
  claimed = models.BooleanField(default=False)

  def __str__(self):
    return self.fullName