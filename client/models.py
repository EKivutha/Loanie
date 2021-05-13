from django.db import models

# Create your models here.

class Loan(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	gurrantor_1 = models.TextField()
	gurrantor_1_ID = models.TextField()
	gurrantor_2 = models.TextField()
	gurrantor_2_ID = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.title

class Payments(models.Model):
	title = models.CharField(max_length=120)
	amount = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.title

class LoanTypes(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.title
