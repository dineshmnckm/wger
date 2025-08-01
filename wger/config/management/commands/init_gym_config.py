
from django.core.management.base import BaseCommand
from wger.config.models import GymConfig


class Command(BaseCommand):
    help = 'Initialize the default GymConfig entry'

    def handle(self, *args, **options):
        # Check if GymConfig with pk=1 exists
        try:
            gym_config = GymConfig.objects.get(pk=1)
            self.stdout.write(self.style.SUCCESS('GymConfig already exists'))
        except GymConfig.DoesNotExist:
            # Create the default GymConfig
            gym_config = GymConfig.objects.create(
                pk=1,
                default_gym=None
            )
            self.stdout.write(self.style.SUCCESS('Successfully created default GymConfig'))
