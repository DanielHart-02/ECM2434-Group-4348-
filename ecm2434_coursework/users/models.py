from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime 
from foodle.models import MealEvent

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE)  
    foodle_score = models.IntegerField(default=0)

    def get_env_score(self):
        score = 0
        for event in MealEvent.objects.filter(group = self.user.groups.first()):
            score += event.score
        return score
    
    env_score = property(get_env_score)

    def __str__(self):  
          return "%s's profile: Score %d" % (self.user, self.foodle_score)

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)