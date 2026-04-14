# Little Lemon API - Implementation Roadmap

## Project Overview
Restaurant booking and menu management system built with Django and MySQL. This document tracks all features and tasks needed to meet project criteria.

---

## Implementation Order (By Priority & Dependencies)

1. **Additional Setup Tasks** - Install djoser, configure DRF (foundation)
2. **User Registration & Authentication** - Djoser setup & User model linking
3. **Menu API Implementation** - Simpler API to start
4. **Table Booking API Implementation** - Complex API with validations
5. **Unit Tests** - Test coverage for all features
6. **Insomnia REST Client Testing** - Manual API verification
7. **Git Repository Setup** - ✅ Already Complete
8. **Django Static HTML Content** - ✅ Already Complete
9. **MySQL & MSSQL Database Connection** - ✅ Already Complete

**SKIPPED (Local Development Only):**
- Environment Variables
- CORS Configuration

---

## 1. Additional Setup Tasks [START HERE]
**Status:** ✅ COMPLETE

- [x] **Install Dependencies:**
  - [x] pipenv install django==4.1.1
  - [x] pipenv install djangorestframework
  - [x] pipenv install django-cors-headers
  - [x] pipenv install python-decouple
  - [x] pipenv install mysqlclient (MySQL driver)
  - [x] pipenv install mssql-django (MSSQL driver)
  - [x] pipenv install pyodbc (ODBC support for MSSQL)
  - [x] pipenv install djoser (User authentication & management)
  - [x] Verified with `pipenv graph`

- [x] **Activate Virtual Environment:**
  - [x] Run `pipenv shell` to activate
  - [x] Use `pipenv run python manage.py <command>` for Django commands

- [ ] **Environment Variables:** (OPTIONAL - Local development only)
  - Skip for local development

- [ ] **CORS Configuration:** (OPTIONAL - Local development only)
  - Skip for local development

- [x] **Django REST Framework Setup:**
  - [x] Add 'rest_framework' to INSTALLED_APPS
  - [x] Add 'rest_framework.authtoken' to INSTALLED_APPS
  - [x] Add rest_framework configuration to settings.py:
    - [x] DEFAULT_AUTHENTICATION_CLASSES = TokenAuthentication
    - [x] DEFAULT_PERMISSION_CLASSES = IsAuthenticated
    - [x] Djoser routes configured in urls.py

- [x] **Admin Interface:**
  - [x] Register Booking model in admin.py
  - [x] Register Menu model in admin.py
  - [x] Admin interface ready at /admin/

---

## 2. Menu API Implementation [THIRD PRIORITY]
**Status:** ⚠️ PARTIAL (Do after authentication is set up)
**Status:** ✅ COMPLETE
- [x] Initialize Git repository in project root
- [x] Create .gitignore file (exclude .env, __pycache__, *.pyc, db.sqlite3, .vs/)
- [x] Make initial commit with current project state
- [x] Push to GitHub remote
- [x] Document Git workflow and commit conventions

---

## 6. Django Static HTML Content Serving
**Status:** ✅ COMPLETE (Already Done)
- [x] HTML templates created (index.html, about.html, menu.html, bookings.html, book.html, menu_item.html)
- [x] Templates directory configured in settings.py
- [x] Views rendering templates with context

---

## 3. MySQL & MSSQL Database Connection
**Status:** ✅ COMPLETE (Already configured, now supporting both)
- [x] MySQL driver configured (django.db.backends.mysql) on localhost:3306
- [x] MSSQL driver configured (mssql via mssql-django) on DESKTOP-AB3PKMH\SQLEXPRESS01
- [x] Database connection settings in settings.py (reservations database in both)
- [x] Connection credentials set up for both
- [x] Configure database routing (if needed for different models)

---

## 2. Menu API Implementation [THIRD PRIORITY]
**Status:** ✅ MOSTLY COMPLETE (85%)

### Current State
- [x] Menu model created with name, price, menu_item_description fields
- [x] Menu views for HTML rendering (menu, display_menu_item)
- [x] Menu serializer (DRF) - All fields included
- [x] Menu viewset with CRUD operations (DRF)
- [x] API endpoints for menu management (/api/menu/)
- [ ] Pagination for menu items (optional)
- [ ] Filtering/search capabilities (optional - use django-filter later)

### API Endpoints Working:
- [x] GET /api/menu/ - List all menu items
- [x] POST /api/menu/ - Create menu item (requires authentication)
- [x] GET /api/menu/{id}/ - Retrieve specific menu item
- [x] PUT /api/menu/{id}/ - Update menu item (requires authentication)
- [x] DELETE /api/menu/{id}/ - Delete menu item (requires authentication)-

## 3. Table Booking API Implementation [FOURTH PRIORITY]

### Current State
- [x] Booking model created (first_name, reservation_date, reservation_slot)
- [x] Basic POST endpoint with double-booking prevention logic
- [x] GET endpoint to retrieve bookings by date
- [x] **DRF Implementation:**
  - [x] Create BookingSerializer
  - [x] Create BookingViewSet with proper permissions

- [x] **API Endpoints:**
  - [x] GET /api/bookings/ (list user's bookings)
  - [x] POST /api/bookings/ (create booking)
  - [x] GET /api/bookings/{id}/ (retrieve specific booking)
  - [x] PUT /api/bookings/{id}/ (update booking)
  - [x] DELETE /api/bookings/{id}/ (cancel booking)

- [x] **Validation & Business Logic:**
  - [x] Prevent past date bookings
  - [x] Double-booking prevention with unique_together constraint
---

## 4. Unit Tests [FIFTH PRIORITY]
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

## 5. Insomnia REST Client Testing [SIXTH PRIORITY]
**Status:** ⚠️ PARTIAL - Endpoints exist but need DRF setup

### Tasks
- [ ] Create Insomnia environment configuration
- [ ] Create Insomnia collection with all endpoints:
  - [ ] User Registration (POST /auth/users/)
  - [ ] User Login (POST /auth/token/login/)
  - [ ] User Logout (POST /auth/token/logout/)
  - [ ] Get User Profile (GET /auth/user/)
  - [ ] Update Profile (PUT /auth/user/)
  - [ ] Change Password (POST /auth/user/set_password/)
  - [ ] List Menus (GET /api/menus/)
  - [ ] Get Menu Item (GET /api/menus/{id}/)
  - [ ] List Bookings (GET /api/bookings/)
  - [ ] Create Booking (POST /api/bookings/)
  - [ ] Update Booking (PUT /api/bookings/{id}/)
  - [ ] Cancel Booking (DELETE /api/bookings/{id}/)
  - [ ] List Tables (GET /api/tables/)
  - [ ] List TimeSlots (GET /api/timeslots/)

- [ ] Test all endpoints in Insomnia
- [ ] Verify token-based authentication works
- [ ] Document API usage in README
- [ ] Export collection for sharing

## 9. Additional Setup Tasks
- [ ] **Install Dependencies:**
  - [ ] pip install djangorestframework
  - [ ] pip install django-cors-headers (for frontend integration)
  - [ ] pip install python-decouple (for environment variables)
  - [ ] Update Pipfile with all dependencies

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

### Phase 1: Foundation (Week 1 - HIGH PRIORITY)
1. **Additional Setup Tasks** - Install DRF, configure environment variables, set up CORS
2. **User Registration & Authentication** - Create auth system and link to User model

### Phase 2: API Development (Week 2-3 - HIGH PRIORITY)
1. **Menu API** - Build simple CRUD endpoints
2. **Table Booking API** - Build complex booking endpoints with validations

### Phase 3: Testing & Polish (Week 3-4 - MEDIUM PRIORITY)
1. **Unit Tests** - Write comprehensive test coverage
2. **Insomnia Testing** - Verify all endpoints work

### Phase 4: Completed (ALREADY DONE)
1. **Git Repository Setup** ✅
2. **Django Static HTML** ✅
3. **MySQL Database** ✅

---

## Implementation Priority (OLD - See "Implementation Order" section above)

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
- [ ] `Pipfile` - Python dependencies (managed by pipenv)
- [ ] `Pipfile.lock` - Locked versions for reproducibility
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
