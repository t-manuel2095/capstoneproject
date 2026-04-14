from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime, timedelta
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


class MenuModelTest(TestCase):
    """Test Menu model functionality"""
    
    def setUp(self):
        """Create test menu items"""
        self.menu_item = Menu.objects.create(
            name='Margherita Pizza',
            price=12,
            menu_item_description='Classic Italian pizza with tomato and mozzarella'
        )
    
    def test_menu_creation(self):
        """Test that menu item is created correctly"""
        self.assertEqual(self.menu_item.name, 'Margherita Pizza')
        self.assertEqual(self.menu_item.price, 12)
        self.assertIn('tomato', self.menu_item.menu_item_description)
    
    def test_menu_str_representation(self):
        """Test menu item string representation"""
        self.assertEqual(str(self.menu_item), 'Margherita Pizza')


class BookingModelTest(TestCase):
    """Test Booking model functionality"""
    
    def setUp(self):
        """Create test booking"""
        tomorrow = timezone.now().date() + timedelta(days=1)
        self.booking = Booking.objects.create(
            first_name='John',
            reservation_date=tomorrow,
            reservation_slot=12,
            party_size=4
        )
    
    def test_booking_creation(self):
        """Test that booking is created correctly"""
        self.assertEqual(self.booking.first_name, 'John')
        self.assertEqual(self.booking.party_size, 4)
        self.assertEqual(self.booking.reservation_slot, 12)
    
    def test_booking_str_representation(self):
        """Test booking string representation"""
        self.assertEqual(str(self.booking), 'John')
    
    def test_booking_party_size_default(self):
        """Test party size default value"""
        tomorrow = timezone.now().date() + timedelta(days=1)
        booking = Booking.objects.create(
            first_name='Jane',
            reservation_date=tomorrow,
            reservation_slot=13
        )
        self.assertEqual(booking.party_size, 1)
    
    def test_unique_together_constraint(self):
        """Test that unique_together prevents double bookings"""
        tomorrow = timezone.now().date() + timedelta(days=1)
        with self.assertRaises(Exception):
            Booking.objects.create(
                first_name='Jane',
                reservation_date=tomorrow,
                reservation_slot=12  # Same slot as setUp booking
            )


class BookingValidationTest(TestCase):
    """Test Booking model validation"""
    
    def test_past_date_validation(self):
        """Test that past dates are rejected"""
        from django.core.exceptions import ValidationError
        yesterday = timezone.now().date() - timedelta(days=1)
        booking = Booking(
            first_name='John',
            reservation_date=yesterday,
            reservation_slot=10
        )
        with self.assertRaises(ValidationError):
            booking.full_clean()
    
    def test_future_date_validation(self):
        """Test that future dates are accepted"""
        tomorrow = timezone.now().date() + timedelta(days=1)
        booking = Booking(
            first_name='John',
            reservation_date=tomorrow,
            reservation_slot=10
        )
        # Should not raise ValidationError
        booking.full_clean()


class MenuSerializerTest(TestCase):
    """Test MenuSerializer"""
    
    def setUp(self):
        self.menu_data = {
            'name': 'Pasta Carbonara',
            'price': 14,
            'menu_item_description': 'Creamy pasta with bacon and eggs'
        }
    
    def test_valid_menu_serializer(self):
        """Test valid menu serializer"""
        serializer = MenuSerializer(data=self.menu_data)
        self.assertTrue(serializer.is_valid())
    
    def test_menu_serializer_creates_object(self):
        """Test that serializer creates menu object"""
        serializer = MenuSerializer(data=self.menu_data)
        self.assertTrue(serializer.is_valid())
        menu = serializer.save()
        self.assertEqual(menu.name, 'Pasta Carbonara')


class BookingSerializerTest(TestCase):
    """Test BookingSerializer"""
    
    def setUp(self):
        tomorrow = (timezone.now() + timedelta(days=1)).date()
        self.booking_data = {
            'first_name': 'Alice',
            'reservation_date': tomorrow,
            'reservation_slot': 15,
            'party_size': 2
        }
    
    def test_valid_booking_serializer(self):
        """Test valid booking serializer"""
        serializer = BookingSerializer(data=self.booking_data)
        self.assertTrue(serializer.is_valid())
    
    def test_past_date_serializer_validation(self):
        """Test that serializer rejects past dates"""
        yesterday = (timezone.now() - timedelta(days=1)).date()
        invalid_data = self.booking_data.copy()
        invalid_data['reservation_date'] = yesterday
        
        serializer = BookingSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('reservation_date', serializer.errors)
    
    def test_double_booking_serializer_validation(self):
        """Test that serializer prevents double bookings"""
        # Create first booking
        tomorrow = (timezone.now() + timedelta(days=1)).date()
        Booking.objects.create(
            first_name='Bob',
            reservation_date=tomorrow,
            reservation_slot=16,
            party_size=2
        )
        
        # Try to create duplicate booking
        duplicate_data = {
            'first_name': 'Charlie',
            'reservation_date': tomorrow,
            'reservation_slot': 16,
            'party_size': 3
        }
        
        serializer = BookingSerializer(data=duplicate_data)
        self.assertFalse(serializer.is_valid())


class MenuAPITest(APITestCase):
    """Test Menu API endpoints"""
    
    def setUp(self):
        """Create test user and menu items"""
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.menu_item1 = Menu.objects.create(
            name='Pizza',
            price=10,
            menu_item_description='Classic pizza'
        )
        self.menu_item2 = Menu.objects.create(
            name='Pasta',
            price=12,
            menu_item_description='Italian pasta'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_get_menu_list(self):
        """Test retrieving menu list"""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_get_menu_detail(self):
        """Test retrieving single menu item"""
        response = self.client.get(f'/api/menu/{self.menu_item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Pizza')
    
    def test_create_menu_item(self):
        """Test creating menu item via API"""
        data = {
            'name': 'Burger',
            'price': 9,
            'menu_item_description': 'Juicy burger'
        }
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
    
    def test_update_menu_item(self):
        """Test updating menu item"""
        data = {'name': 'Premium Pizza', 'price': 15, 'menu_item_description': 'Upgraded pizza'}
        response = self.client.put(f'/api/menu/{self.menu_item1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item1.refresh_from_db()
        self.assertEqual(self.menu_item1.price, 15)
    
    def test_delete_menu_item(self):
        """Test deleting menu item"""
        response = self.client.delete(f'/api/menu/{self.menu_item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)


class BookingAPITest(APITestCase):
    """Test Booking API endpoints"""
    
    def setUp(self):
        """Create test user and booking"""
        self.user = User.objects.create_user(username='testuser', password='pass123')
        tomorrow = (timezone.now() + timedelta(days=1)).date()
        self.booking = Booking.objects.create(
            first_name='Test User',
            reservation_date=tomorrow,
            reservation_slot=10,
            party_size=2
        )
        self.client.force_authenticate(user=self.user)
    
    def test_get_bookings_list(self):
        """Test retrieving bookings list"""
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_booking(self):
        """Test creating booking via API"""
        tomorrow = (timezone.now() + timedelta(days=2)).date()
        data = {
            'first_name': 'New Booking',
            'reservation_date': tomorrow,
            'reservation_slot': 12,
            'party_size': 3
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_booking_past_date_rejected(self):
        """Test that API rejects bookings with past dates"""
        yesterday = (timezone.now() - timedelta(days=1)).date()
        data = {
            'first_name': 'Invalid Booking',
            'reservation_date': yesterday,
            'reservation_slot': 10,
            'party_size': 2
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_double_booking_rejected(self):
        """Test that double bookings are rejected"""
        tomorrow = (timezone.now() + timedelta(days=1)).date()
        data = {
            'first_name': 'Another User',
            'reservation_date': tomorrow,
            'reservation_slot': 10,  # Same slot as setUp booking
            'party_size': 2
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AuthenticationTest(APITestCase):
    """Test authentication and permissions"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
    
    def test_unauthenticated_access_denied(self):
        """Test that unauthenticated users are denied access"""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authenticated_access_allowed(self):
        """Test that authenticated users have access"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class IntegrationTest(APITestCase):
    """Integration tests for complete workflows"""
    
    def setUp(self):
        """Create test user"""
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.force_authenticate(user=self.user)
    
    def test_complete_booking_workflow(self):
        """Test complete booking workflow: view menu -> create booking"""
        # Step 1: Browse menu
        Menu.objects.create(name='Pizza', price=10, menu_item_description='Good pizza')
        menu_response = self.client.get('/api/menu/')
        self.assertEqual(menu_response.status_code, status.HTTP_200_OK)
        
        # Step 2: Create booking
        tomorrow = (timezone.now() + timedelta(days=1)).date()
        booking_data = {
            'first_name': 'Integration Test',
            'reservation_date': tomorrow,
            'reservation_slot': 18,
            'party_size': 4
        }
        booking_response = self.client.post('/api/bookings/', booking_data)
        self.assertEqual(booking_response.status_code, status.HTTP_201_CREATED)
        
        # Step 3: Verify booking was created
        final_response = self.client.get('/api/bookings/')
        self.assertEqual(final_response.status_code, status.HTTP_200_OK)
