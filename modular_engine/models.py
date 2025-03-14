from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50, default="1.0")
    is_installed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"
