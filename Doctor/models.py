from django.db import models


# Create your models here.

class doctor(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Enter a valid email address.")
        if not username:
            raise ValueError("Enter a valid email username.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user .save(using=self._db)
        return user
