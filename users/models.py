from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = "users"
