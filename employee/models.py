from django.db import models


# Create your models here.
class Person(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    idcard = models.CharField(max_length=35, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    birth_of_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    birth_city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    bank_account = models.CharField(max_length=20, null=True, blank=True)
    marital = models.BooleanField(default=False)
    tax_account = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    reg_number = models.CharField(max_length=15, unique=True)
    number_bpjstk = models.CharField(max_length=20, null=True, blank=True)
    number_bpjskes = models.CharField(max_length=20, null=True, blank=True)
    date_of_hired = models.DateField()
    is_permanent = models.BooleanField(default=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.reg_number, self.person.name)


class Leader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, null=False)
    jabatan = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class EmailGroup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Group(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(Leader, on_delete=models.PROTECT)
    employee = models.ManyToManyField(Employee, through='GroupEmployee')
    #email_group = models.ForeignKey(NotifyEmailGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class RegisterEmailGroup(models.Model):
    email_group = models.ForeignKey(EmailGroup, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_group.email


class GroupEmployee(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)


class NotifyEmail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name