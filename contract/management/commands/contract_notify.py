from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.db.models import Q, F

from contract.models import Contract
from employee.models import GroupEmployee


class Command(BaseCommand):
    help = "Notify due date contracts"

    def handle(self, *args, **options):
        today = datetime.today().date()
        day_range = 30
        lookup_range = today + timedelta(days=day_range)

        contracts = Contract.objects.filter(
            Q(status='notified') |
            Q(end_date__range=(today, lookup_range))
        ).select_related('employee')

        contracts.update(status='notified')

        data = {}

        for c in contracts:
            try:
                if c.employee.groupemployee.group.name in data:
                    data[c.employee.groupemployee.group.name]['group'] = c.employee.groupemployee.group
                    data[c.employee.groupemployee.group.name]['contracts'].append(c)
                else:
                    data[c.employee.groupemployee.group.name] = {
                        'group': c.employee.groupemployee.group,
                        'contracts': [],
                        'emails': c.employee.groupemployee.group.registeremailgroup_set.all()
                    }
                    data[c.employee.groupemployee.group.name]['contracts'].append(c)
            except GroupEmployee.DoesNotExist:
                msg = "<{}> in contract <{}> has no <GroupEmployee> related objects".format(
                    c.employee.person.name, c.number_contract
                )
                print(msg)

        print(data)
