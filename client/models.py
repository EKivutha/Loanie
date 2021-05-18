from django.db import models

# Create your models here.
class LoanTypes(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	class Meta:
        # Gives the proper plural name for admin
		verbose_name_plural = "types"

	def __str__(self):
		return self.loan_title

class Loan(models.Model):
	loan_title = models.ForeignKey(LoanTypes, default=0, verbose_name="types", on_delete=models.SET_DEFAULT)
	reason = models.TextField()
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


