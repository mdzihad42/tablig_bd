from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name='members')
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gasht(models.Model):
    GASHT_TYPE_CHOICES = [
        ('public', 'উমুমী গাশত'),
        ('personal', 'খুসুসী গাশত'),
    ]

    date = models.DateField()
    gasht_type = models.CharField(max_length=20, choices=GASHT_TYPE_CHOICES)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='gashts')
    amir = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='gashts_as_amir')
    rahbar = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='gashts_as_rahbar')
    mutakallim = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='gashts_as_mutakallim')
    participants = models.ManyToManyField(Member, related_name='participated_gashts', blank=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_gasht_type_display()} - {self.date} ({self.area.name})"
