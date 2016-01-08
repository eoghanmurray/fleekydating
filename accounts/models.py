from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
import datetime
from django.conf import settings



class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):

        now = timezone.now()

        if not email:

            raise ValueError('The given username must be set')

        email = self.normalize_email(email)




        user = self.model(username=email, email=email,
                        is_staff=is_staff, is_active=True,
                        is_superuser=is_superuser,
                        date_joined=now, **extra_fields)


        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractUser):

    CHOICES=[('Male','Male'),
         ('Female','Female')]

    CHOICES2 =[('Athletic','Athletic'),
         ('Academic','Academic'),
             ('Musical', 'Musical')]

    CHOICES3 =[('Trinity','Trinity'),
         ('DIT','DIT'),
             ('UCD', 'UCD'),
               ('IADT', 'IADT'),
               ('NUIG', 'NUIG'),
               ('UL', 'UL'),
               ('NUI', 'NUI')]

    CHOICES4 =[('Dublin','Dublin'),
         ('Cork','Cork'),
             ('Galway', 'Galway'),
               ('Belfast', 'Belfast'),
               ('Limerick', 'Limerick'),]

    first_login = models.BooleanField(default=True)
    profileimage = models.ImageField(upload_to='images', blank=True)
    gender = models.CharField(max_length=6, choices=CHOICES, null=True)
    seeking = models.CharField(max_length=6, choices=CHOICES, null=True)
    living = models.CharField(max_length=8, choices=CHOICES4, null=True)
    university = models.CharField(max_length=8, choices=CHOICES3, null=True)
    likes = models.CharField(max_length=8, choices=CHOICES2, null=True)
    date_of_birth = models.DateField(default=datetime.date.today)


    objects = AccountUserManager()


class Status(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=2000, blank=True, null=True)
    created_date = models.DateTimeField( default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()



class Crush(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="crush_creator_set")
    crush = models.ForeignKey(User, related_name="crush_set")
    points = models.IntegerField(default=0)




class Likers(models.Model):

    status = models.ForeignKey(Status)
    liker = models.ForeignKey(User, related_name="liker")



class Dislikers(models.Model):

    status = models.ForeignKey(Status)
    disliker = models.ForeignKey(User, related_name="disliker")



class Wink(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    initiator = models.ForeignKey(User, related_name="wink_initiator_set")
    receiver = models.ForeignKey(User, related_name="wink_receiver_set")


class Notification(models.Model):

    message = models.CharField(max_length=50)
    viewed =  models.BooleanField(default=False)
    user = models.ForeignKey(User)













