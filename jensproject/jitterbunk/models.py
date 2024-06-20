from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to+')
    time = models.DateTimeField()

    def __str__(self):
        return str(self.from_user) + " bunked " + str(self.to_user)
    
class Bunkform(models.Model):
    bunker = models.CharField(max_length=200)
    bunked = models.CharField(max_length=200)


