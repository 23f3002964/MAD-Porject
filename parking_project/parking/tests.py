from django.test import TestCase
from django.urls import reverse
from .models import ParkingSpot

class ParkingSpotModelTests(TestCase):
    """
    Tests for the ParkingSpot model.
    """
    def test_parking_spot_creation_defaults(self):
        """
        Test that a ParkingSpot object is created with default values.
        'is_available' should default to True.
        'size' should default to 'M'.
        """
        spot = ParkingSpot.objects.create(
            spot_number="T01",
            location_description="Test Location 1"
        )
        self.assertEqual(spot.spot_number, "T01")
        self.assertEqual(spot.location_description, "Test Location 1")
        self.assertTrue(spot.is_available) # Default is True
        self.assertEqual(spot.size, 'M') # Default is 'M'
        self.assertIsNotNone(spot.created_at)
        self.assertIsNotNone(spot.updated_at)

    def test_parking_spot_str_representation(self):
        """
        Test the __str__ method of the ParkingSpot model.
        """
        spot_available = ParkingSpot.objects.create(
            spot_number="T02",
            location_description="Test Location 2, Available",
            size="L",
            is_available=True
        )
        self.assertEqual(str(spot_available), "T02 (Large) - Available")

        spot_occupied = ParkingSpot.objects.create(
            spot_number="T03",
            location_description="Test Location 3, Occupied",
            size="S",
            is_available=False
        )
        self.assertEqual(str(spot_occupied), "T03 (Small) - Occupied")


class ParkingViewsTests(TestCase):
    """
    Tests for the parking app views.
    """
    @classmethod
    def setUpTestData(cls):
        # Create some parking spots for view tests
        cls.spot1 = ParkingSpot.objects.create(spot_number="V01", location_description="View Test Spot 1", size="M", is_available=True)
        cls.spot2 = ParkingSpot.objects.create(spot_number="V02", location_description="View Test Spot 2", size="S", is_available=False)
        cls.spot3 = ParkingSpot.objects.create(spot_number="V03", location_description="View Test Spot 3", size="L", is_available=True)

    def test_available_spots_list_view_status_code(self):
        """
        Test that the available_spots_list view returns a 200 OK status code.
        """
        response = self.client.get(reverse('parking:available_spots_list'))
        self.assertEqual(response.status_code, 200)

    def test_available_spots_list_view_uses_correct_template(self):
        """
        Test that the available_spots_list view uses the correct template.
        """
        response = self.client.get(reverse('parking:available_spots_list'))
        self.assertTemplateUsed(response, 'parking/available_spots_list.html')

    def test_available_spots_list_view_displays_only_available_spots(self):
        """
        Test that only available spots are listed and passed to the template.
        """
        response = self.client.get(reverse('parking:available_spots_list'))
        self.assertIn('available_spots', response.context)
        available_spots_in_context = response.context['available_spots']
        
        self.assertEqual(len(available_spots_in_context), 2)
        self.assertIn(self.spot1, available_spots_in_context)
        self.assertIn(self.spot3, available_spots_in_context)
        self.assertNotIn(self.spot2, available_spots_in_context) # spot2 is not available

        # Check content as well to be sure
        self.assertContains(response, self.spot1.spot_number)
        self.assertContains(response, self.spot3.spot_number)
        self.assertNotContains(response, self.spot2.spot_number)

    def test_available_spots_list_view_no_spots_message(self):
        """
        Test the 'no spots available' message when no spots are available.
        """
        # Make all spots unavailable
        ParkingSpot.objects.all().update(is_available=False)
        
        response = self.client.get(reverse('parking:available_spots_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('available_spots', response.context)
        self.assertEqual(len(response.context['available_spots']), 0)
        self.assertContains(response, "No parking spots are currently available.")

    def test_available_spots_list_view_empty_db(self):
        """
        Test the 'no spots available' message when the database is empty.
        """
        ParkingSpot.objects.all().delete() # Clear all spots
        
        response = self.client.get(reverse('parking:available_spots_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('available_spots', response.context)
        self.assertEqual(len(response.context['available_spots']), 0)
        self.assertContains(response, "No parking spots are currently available.")
