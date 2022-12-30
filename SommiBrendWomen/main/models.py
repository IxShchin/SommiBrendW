from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return "Пароль %s %s" % (self.password, self.email)