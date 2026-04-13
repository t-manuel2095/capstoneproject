# Little Lemon API - Implementation Roadmap

## Project Overview
Restaurant booking and menu management system built with Django and MySQL. This document tracks all features and tasks needed to meet project criteria.

---

## 1. Git Repository Setup
- [ ] Initialize Git repository in project root
- [ ] Create .gitignore file (exclude .env, __pycache__, *.pyc, db.sqlite3)
- [ ] Make initial commit with current project state
- [ ] Document Git workflow and commit conventions

---

## 2. Django Static HTML Content Serving
**Status:** ✅ COMPLETE
- [x] HTML templates created (index.html, about.html, menu.html, bookings.html, book.html, menu_item.html)
- [x] Templates directory configured in settings.py
- [x] Views rendering templates with context

---

## 3. MySQL Database Connection
**Status:** ✅ COMPLETE
- [x] MySQL driver configured (django.db.backends.mysql)
- [x] Database connection settings in settings.py (reservations database)
- [x] Connection credentials set up (admindjango user)

---

## 4. Menu API Implementation
**Status:** ⚠️ PARTIAL - Needs Django REST Framework

### Current State
- [x] Menu model created with name, price, menu_item_description fields
- [x] Menu views for HTML rendering (menu, display_menu_item)
- [ ] Menu serializer (DRF)
- [ ] Menu viewset with CRUD operations (DRF)
- [ ] API endpoints for menu management
- [ ] Pagination for menu items
- [ ] Filtering/search capabilities
- [ ] Insomnia collection for menu endpoints

---

## 5. Table Booking API Implementation
**Status:** ⚠️ PARTIAL - Needs Enhancements

### Current State
- [x] Booking model created (first_name, reservation_date, reservation_slot)
- [x] Basic POST endpoint with double-booking prevention logic
- [x] GET endpoint to retrieve bookings by date
- [ ] **Model Enhancements:**
  - [ ] Add ForeignKey to User model
  - [ ] Add email field
  - [ ] Add phone_number field
  - [ ] Add party_size field
  - [ ] Add last_name field
  - [ ] Add special_requests field (optional)

- [ ] **Create Table Model:**
  - [ ] Add Table model with table_number, capacity, location fields
  - [ ] Link Booking to Table via ForeignKey

- [ ] **Create TimeSlot Model:**
  - [ ] Add TimeSlot model with start_time, end_time fields
  - [ ] Link Booking to TimeSlot
  - [ ] Replace SmallIntegerField approach

- [ ] **DRF Implementation:**
  - [ ] Create BookingSerializer
  - [ ] Create TableSerializer
  - [ ] Create TimeSlotSerializer
  - [ ] Create BookingViewSet with proper permissions
  - [ ] Create TableViewSet

- [ ] **API Endpoints:**
  - [ ] GET /api/bookings/ (list user's bookings)
  - [ ] POST /api/bookings/ (create booking)
  - [ ] GET /api/bookings/{id}/ (retrieve specific booking)
  - [ ] PUT /api/bookings/{id}/ (update booking)
  - [ ] DELETE /api/bookings/{id}/ (cancel booking)
  - [ ] GET /api/tables/ (available tables)
  - [ ] GET /api/timeslots/ (available time slots)

- [ ] **Validation & Business Logic:**
  - [ ] Prevent past date bookings
  - [ ] Double-booking prevention with unique_together constraint
  - [ ] Validate party_size against table capacity
  - [ ] Validate reservation_slot exists

- [ ] **Remove Security Issues:**
  - [ ] Remove @csrf_exempt decorator from bookings view
  - [ ] Use proper DRF authentication/CSRF handling

---

## 6. User Registration & Authentication
**Status:** ❌ NOT STARTED

### Tasks
- [ ] **Django User Model Integration:**
  - [ ] Link User model to Booking (ForeignKey)
  - [ ] Link User model to Menu (for admin/staff)

- [ ] **User Registration:**
  - [ ] Create UserSerializer
  - [ ] Create registration viewset/endpoint (POST /api/register/)
  - [ ] Implement password validation
  - [ ] Send confirmation email (optional)

- [ ] **Authentication Setup:**
  - [ ] Install Django REST Framework
  - [ ] Configure TokenAuthentication
  - [ ] Create login endpoint (POST /api/login/)
  - [ ] Create logout endpoint (POST /api/logout/)
  - [ ] Create token refresh mechanism

- [ ] **Permission Classes:**
  - [ ] Create IsOwnerOrReadOnly permission
  - [ ] Create IsAuthenticated checks
  - [ ] Apply permissions to all endpoints

- [ ] **API Endpoints:**
  - [ ] POST /api/register/ (user registration)
  - [ ] POST /api/login/ (obtain token)
  - [ ] POST /api/logout/ (destroy token)
  - [ ] GET /api/user/ (current user profile)
  - [ ] PUT /api/user/ (update profile)

---

## 7. Unit Tests
**Status:** ❌ NOT STARTED

### Test Coverage Required

- [ ] **Model Tests:**
  - [ ] Test Booking model creation
  - [ ] Test Menu model creation
  - [ ] Test User-Booking relationship
  - [ ] Test Table-Booking relationship
  - [ ] Test TimeSlot model
  - [ ] Test validation constraints

- [ ] **View/API Tests:**
  - [ ] Test Menu list endpoint
  - [ ] Test Menu detail endpoint
  - [ ] Test Booking creation
  - [ ] Test double-booking prevention
  - [ ] Test user can only see own bookings
  - [ ] Test unauthorized access is blocked
  - [ ] Test invalid date/slot rejection
  - [ ] Test party_size validation

- [ ] **Authentication Tests:**
  - [ ] Test user registration
  - [ ] Test user login
  - [ ] Test token generation
  - [ ] Test authenticated vs unauthenticated access
  - [ ] Test permission enforcement

- [ ] **Integration Tests:**
  - [ ] Test full booking flow (register → login → create booking)
  - [ ] Test menu browsing and booking together

### Test Targets
- Aim for 90%+ code coverage
- Use Django TestCase and APITestCase
- Create fixtures for test data
- File: restaurant/tests.py

---

## 8. Insomnia REST Client Testing
**Status:** ⚠️ PARTIAL - Endpoints exist but need DRF setup

### Tasks
- [ ] Create Insomnia environment configuration
- [ ] Create Insomnia collection with all endpoints:
  - [ ] User Registration (POST)
  - [ ] User Login (POST)
  - [ ] List Menus (GET)
  - [ ] Get Menu Item (GET)
  - [ ] List Bookings (GET)
  - [ ] Create Booking (POST)
  - [ ] Update Booking (PUT)
  - [ ] Cancel Booking (DELETE)
  - [ ] List Tables (GET)
  - [ ] List TimeSlots (GET)

- [ ] Test all endpoints in Insomnia
- [ ] Document API usage in README
- [ ] Export collection for sharing

---

## 9. Additional Setup Tasks
- [ ] **Install Dependencies:**
  - [ ] pip install djangorestframework
  - [ ] pip install django-cors-headers (for frontend integration)
  - [ ] pip install python-decouple (for environment variables)
  - [ ] Update requirements.txt

- [ ] **Environment Variables:**
  - [ ] Move database credentials to .env
  - [ ] Move SECRET_KEY to .env
  - [ ] Create .env.example

- [ ] **CORS Configuration:**
  - [ ] Install and configure django-cors-headers
  - [ ] Allow frontend domain(s)

- [ ] **Admin Interface:**
  - [ ] Register models in admin.py
  - [ ] Create admin views for booking management
  - [ ] Create admin views for menu management

- [ ] **Documentation:**
  - [ ] Create API documentation (endpoints, methods, responses)
  - [ ] Create README with setup instructions
  - [ ] Create CONTRIBUTING guidelines
  - [ ] Document database schema

---

## Implementation Priority

### Phase 1: Foundation (High Priority)
1. Initialize Git repository
2. Install Django REST Framework & dependencies
3. Move credentials to environment variables
4. Enhance Booking model with user/contact fields
5. Create Table and TimeSlot models

### Phase 2: Authentication & Security (High Priority)
1. Link Booking to User model
2. Create user registration/login endpoints
3. Implement TokenAuthentication
4. Add permission classes to all endpoints
5. Remove @csrf_exempt decorator

### Phase 3: API Development (Medium Priority)
1. Create serializers for all models
2. Create viewsets with proper endpoints
3. Implement validation and business logic
4. Add filtering and pagination
5. Test all endpoints with Insomnia

### Phase 4: Testing & Polish (Medium Priority)
1. Write unit tests for models
2. Write API endpoint tests
3. Write authentication tests
4. Achieve 90%+ code coverage
5. Document API and setup process

---

## Success Criteria Checklist

- [ ] Django serves static HTML content
- [ ] Project committed to Git repository
- [ ] Application connects to MySQL database
- [ ] Menu API fully implemented (DRF)
- [ ] Table booking API fully implemented (DRF)
- [ ] User registration and authentication working
- [ ] Unit tests written (90%+ coverage)
- [ ] All endpoints testable with Insomnia
- [ ] No security vulnerabilities (@csrf_exempt removed)
- [ ] Comprehensive documentation provided

---

## Notes & Blockers

- **Current Blocker:** Django REST Framework not installed
- **Security Issue:** @csrf_exempt on bookings endpoint needs to be removed
- **Data Issue:** Booking model lacks user association
- **Testing Gap:** No tests currently written

---

## Files to Create/Modify

### Create New Files
- [ ] `restaurant/serializers.py` - DRF serializers
- [ ] `restaurant/permissions.py` - Custom permission classes
- [ ] `Implementation_Roadmap.md` - This file
- [ ] `.env` - Environment variables
- [ ] `.env.example` - Environment template
- [ ] `requirements.txt` - Python dependencies
- [ ] `API_DOCUMENTATION.md` - API endpoint documentation
- [ ] `SETUP.md` - Setup and installation guide

### Modify Existing Files
- [ ] `restaurant/models.py` - Add User FK, new fields, new models
- [ ] `restaurant/views.py` - Refactor to use DRF viewsets
- [ ] `restaurant/admin.py` - Register all models
- [ ] `restaurant/tests.py` - Add comprehensive tests
- [ ] `littlelemon/settings.py` - Add DRF config, CORS, environment variables
- [ ] `littlelemon/urls.py` - Add API routes
- [ ] `restaurant/forms.py` - Update if needed

---

Last Updated: April 10, 2026
