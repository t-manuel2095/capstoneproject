# MSSQL Connection Troubleshooting

## Issue
Django application fails to connect to SQL Server (MSSQL) instance `DESKTOP-AB3PKMH\SQLEXPRESS01` when running `python manage.py runserver`.

## Server Details
- Server Name: `DESKTOP-AB3PKMH\SQLEXPRESS01`
- Database: `reservations`
- Username: `mt`
- Password: `nfltop100`
- ODBC Driver: ODBC Driver 17 for SQL Server

## Explicit Error
```
pyodbc.OperationalError: ('08001', '[08001] [Microsoft][ODBC Driver 17 for SQL Server]
Named Pipes Provider: Could not open a connection to SQL Server [2]. (2) (SQLDriverConnect); 
[08001] [Microsoft][ODBC Driver 17 for SQL Server]Login timeout expired (0); 
[08001] [Microsoft][ODBC Driver 17 for SQL Server]Invalid connection string attribute (0); 
[08001] [Microsoft][ODBC Driver 17 for SQL Server]A network-related or instance-specific error 
has occurred while establishing a connection to SQL Server. Server is not found or not accessible. 
Check if instance name is correct and if SQL Server is configured to allow remote connections. 
For more information see SQL Server Books Online. (2)')
```

## Solutions Attempted

### 1. Initial Configuration (Failed)
**Configuration Used:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root@123',
    }
}
```
**Issue:** User wanted MSSQL, not MySQL.

---

### 2. MSSQL with django-pyodbc-azure Backend (Failed)
**Configuration Used:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'reservations',
        'HOST': 'DESKTOP-AB3PKMH\\SQLEXPRESS01',
        'PORT': '1433',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'Trusted_Connection': 'yes',
        }
    }
}
```
**Issues:**
- Dependency conflict: `django-pyodbc-azure` requires Django 2.1.x, which is too old for Python 3.14
- After upgrading Django, `django-pyodbc-azure` became incompatible

---

### 3. Switched to mssql-django Backend (Still Failing)
**Backend Changed:** Replaced `django-pyodbc-azure` with `mssql-django`

**Configuration Attempt 1:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'reservations',
        'HOST': 'DESKTOP-AB3PKMH',
        'PORT': '1433',
        'USER': 'mt',
        'PASSWORD': 'nfltop100',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'Trusted_Connection': 'yes',
            'MARS_Connection': 'yes',
            'Instance': 'SQLEXPRESS01',
        }
    }
}
```
**Error:** Invalid connection string attribute

---

### 4. Simplified Configuration with Localhost (Failed)
**Configuration Attempt 2:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'reservations',
        'HOST': '.',
        'USER': 'mt',
        'PASSWORD': 'nfltop100',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}
```
**Error:** Named Pipes Provider: Could not open a connection

---

### 5. Using Exact Server Name from SSMS (✅ SUCCESS!)
**Configuration Attempt 3:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'reservations',
        'HOST': 'DESKTOP-AB3PKMH\\SQLEXPRESS01',
        'USER': 'mt',
        'PASSWORD': 'nfltop100',
    }
}
```
**Status:** ✅ WORKING - Connection established successfully!

**Key Learning:** The simple configuration without OPTIONS worked best. The issue was likely that the OPTIONS (driver, Trusted_Connection, etc.) were causing "Invalid connection string attribute" errors with `mssql-django`.

---

## Potential Root Causes
1. **Named Pipes vs TCP Protocol:** SQL Server may not be configured to accept connections on the protocol being used
2. **Connection String Format:** `mssql-django` may not accept the instance name in the HOST field
3. **SQL Server Service:** SQL Server service may not be running or accessible
4. **Firewall/Network:** Network connectivity issues preventing connection

---

## Next Steps
1. ✅ Django is now connected to MSSQL
2. Run migrations: `python manage.py migrate`
3. Test the application by accessing it in your browser
4. Create the Booking and Menu tables (or let Django handle it via migrations)
