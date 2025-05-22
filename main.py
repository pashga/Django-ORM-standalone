import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcard_all = Passcard.objects.all()
    passcard_filter = Passcard.objects.filter(is_active=True)
    print('Всего пропусков', len(passcard_all))
    print('Активных пропусков', len(passcard_filter))

