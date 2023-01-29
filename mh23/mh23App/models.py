from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager

class Events(models.Model):
	group = models.ForeignKey(
		'Groups', models.DO_NOTHING, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	date_of_event = models.DateField(blank=True, null=True)
	location = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'events'


class Categories(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'categories'


class GroupCategories(models.Model):
	group = models.ForeignKey(
		'Groups', models.DO_NOTHING, blank=True, null=True)
	category = models.ForeignKey(
		Categories, models.DO_NOTHING, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'group_categories'


class Groups(models.Model):
	user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True, related_name='+')
	# This field type is a guess.
	user_ids = models.TextField(blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'groups'


class Posts(models.Model):
	event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
	header = models.CharField(max_length=25, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='images/')
	location = models.IntegerField(blank=True, null=True)
	comments = models.CharField(max_length=500)

	class Meta:
		managed = False
		db_table = 'posts'


class Users(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=100, blank=True, null=True, unique=True)
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	dob = models.DateField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	class Meta:
		managed = False
		db_table = 'users'

	def str(self):
		return self.email



class Comments(models.Model):
	post = models.ForeignKey('Posts', models.DO_NOTHING, blank=True, null=True, related_name='+')
	user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
	comment = models.CharField(max_length=500, blank=True, null=True)
	comment_id = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'comments'
