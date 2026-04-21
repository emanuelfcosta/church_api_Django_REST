from django.db import models


class Church(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    foundationdate = models.DateField()
    cnpj = models.CharField(max_length=18)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Member(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='members')

    status = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    baptismdate = models.DateField()
    addmission = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    birthdate = models.DateField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Financial(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    theDate = models.DateField()
    paymentMethod = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type} - {self.amount}"

class Occasion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name

class Prayer(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('answered', 'Respondida'),
    ]

    reason = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.reason

class Study(models.Model):
    theDate = models.DateField()
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    notes = models.TextField()

    def __str__(self):
        return self.subject



