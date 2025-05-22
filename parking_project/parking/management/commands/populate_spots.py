from django.core.management.base import BaseCommand, CommandError
from parking.models import ParkingSpot

class Command(BaseCommand):
    help = 'Populates the database with initial parking spot data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate parking spots...'))

        spots_data = [
            {'spot_number': 'A01', 'location_description': 'Level 1, near main entrance', 'size': 'S', 'is_available': True},
            {'spot_number': 'A02', 'location_description': 'Level 1, near main entrance', 'size': 'M', 'is_available': False},
            {'spot_number': 'B05', 'location_description': 'Level 2, by the west wall, column 5', 'size': 'M', 'is_available': True},
            {'spot_number': 'C12', 'location_description': 'Covered spot, Level 3, near elevator', 'size': 'L', 'is_available': True},
            {'spot_number': 'D07', 'location_description': 'Rooftop, uncovered, section D', 'size': 'L', 'is_available': False},
            {'spot_number': 'E01', 'location_description': 'Basement Level 1, compact cars only', 'size': 'S', 'is_available': True},
        ]

        created_count = 0
        skipped_count = 0

        for spot_data in spots_data:
            spot, created = ParkingSpot.objects.get_or_create(
                spot_number=spot_data['spot_number'],
                defaults={
                    'location_description': spot_data['location_description'],
                    'size': spot_data['size'],
                    'is_available': spot_data['is_available']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created parking spot: {spot.spot_number}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Parking spot {spot.spot_number} already exists. Skipped.'))
                skipped_count += 1

        self.stdout.write(self.style.SUCCESS(f'Finished populating spots. {created_count} created, {skipped_count} skipped.'))
