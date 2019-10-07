from django.db import models

from django_fsm import FSMField, transition

from employee.models import Employee
from project.models import Project

# Create your models here.
class ContractType(models.Model):
    contract_name = models.CharField(max_length=20, unique=True)
    contract_description = models.CharField(max_length=255)

    def __str__(self):
        return self.contract_name


class Jabatan(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Jabatan"


class Contract(models.Model):
    number_contract = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    contract_type = models.ForeignKey(ContractType, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True, blank=True)
    doc_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    contract_distance = models.PositiveIntegerField()
    besar_upah = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    corporate_name = models.CharField(max_length=100, null=True, blank=True)
    corporate_address = models.CharField(max_length=100, null=True, blank=True)
    jenis_usaha = models.CharField(max_length=50, null=True, blank=True)
    cara_pembayaran = models.CharField(max_length=50, null=True, blank=True)
    tempat_aggrement = models.CharField(max_length=100, null=True, blank=True)
    pejabat_acc = models.CharField(max_length=100, null=True, blank=True)
    status = FSMField(default='active')

    def __str__(self):
        return self.number_contract

    @transition(field=status, source='active', target='notified')
    def set_notified(self):
        """
        Set contracts from active state to be notified stated.
        Notified state means that this contract need to be notified
        to user by email.
        :return: None
        """
        pass

    @transition(field=status, source='notified', target='closed')
    def set_closed(self):
        """
        Set contracts from notified state to closed state.
        Closed state means that this contract is old, and new contract
        has been created.
        :return: None
        """
        pass
