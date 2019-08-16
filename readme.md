## Automation API for TATA Main Hospital, Jamshedpur

### Introduction

Tata Main Hospital (TMH), Jamshedpur serves millions of customers each year using both its offline and online services. The automation endpoint for TMH Vishwas serves the following purpose:

+ Appointment booking/cancellation using IOT devices
+ Upcoming appointment listing
+ Push emergency alerts to TMH server  
+ Classified endpoints

### Prerequisites

+ Django 2.2
+ Django rest framework
+ Python 3
+ Heroku

### API Specifications

The API in repository is intended to be used for testing purpose only. No registration done using the API service would affect any resources or records on the main server. However, this may be used to lay foundations of the integrated version of the same into the TMH Vishwas platform.

#### List of Endpoints

Given below are the list of available endpoints in the current API version v1
+ Get all users' list [PRIVILEDGE] : https://tmhvishwas.herokuapp.com/api/users/
+ Get all Group list [PRIVILEDGE]: https://tmhvishwas.herokuapp.com/api/groups/

**Automation API (v1) endpoints**
+ Avail general booking: https://tmhvishwas.herokuapp.com/api/v1/appointments/
+ Avail emergency booking: https://tmhvishwas.herokuapp.com/api/v1/emergency/

Alternatively, a JSON response of API endpoints are available at endpoint: `/api`

```JSON
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "users": "https://tmhvishwas.herokuapp.com/api/users/",
    "groups": "https://tmhvishwas.herokuapp.com/api/groups/",
    "v1/appointments": "https://tmhvishwas.herokuapp.com/api/v1/appointments/",
    "v1/emergency": "https://tmhvishwas.herokuapp.com/api/v1/emergency/"
}
```
