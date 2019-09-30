from django.db import models
from users.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)


class UploadReports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    xls = models.FileField(upload_to=user_directory_path)
