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

class Talim(models.Model):
    date = models.DateField()
    book_name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, blank=True, null=True)
    performed_by = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='talims_given')
    participants = models.ManyToManyField(Member, related_name='talims_attended')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Talim: {self.book_name} - {self.date}"

class Finance(models.Model):
    TYPE_CHOICES = [
        ('income', 'আয় (Income)'),
        ('expense', 'ব্যয় (Expense)'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100) # e.g., Mosque Fund, Safar, Food
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True) # Linked to a member if it's a donation

    def __str__(self):
        return f"{self.get_type_display()}: {self.amount} ({self.date})"

class Jamat(models.Model):
    TYPE_CHOICES = [
        ('3day', '৩ দিন'),
        ('10day', '১০ দিন'),
        ('40day', 'চিল্লা (৪০ দিন)'),
        ('4month', '৪ মাস'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='jamats')
    jamat_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default='ongoing') # ongoing, completed, cancelled
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.member.name} - {self.get_jamat_type_display()}"
