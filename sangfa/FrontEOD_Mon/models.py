from django.db import models
from django.contrib.auth.models import User


class Host(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=50, help_text="Host Name")
    # email = models.EmailField()
    # poll_time = models.AutoField()
    cpu = models.CharField(max_length=20, blank=True, editable=False)
    ram = models.CharField(max_length=20, blank=True, editable=False)
    diskio = models.CharField(max_length=50, blank=True, editable=False)
    conf_location = models.CharField(max_length=50)
    description = models.CharField(u'Site Description', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname

    def get_cpu(self):
        return "%s" % self.cpu

    def get_ram(self):
        return "%s" % self.ram


class Tool(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=20, help_text="Tool Name")
    log_location = models.CharField(max_length=20, blank=True)
    log_info = models.CharField('Log', max_length=200, blank=True, editable=True)
    # poll_time = models.AutoField()
    # email = models.EmailField()
    description = models.CharField(u'Device Description', max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str_(self):
        return self.device_code

    def get_tool_name(self):
        return "%s" % self.tool_name

    def get_log(self):
        return "%s" % self.log_info
