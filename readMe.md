# Django User Registration and Login API 

## Introduction

This is a simple API for user registration and authentication, written with Django and Django Rest Framework.
It is a *PASSWORDLESS* authentication system and USERNAME_FIELD is the *EMAIL*. 

## How It Works

The API accepts email and fullname fields only. No other field is hardcoded by client. You can modify the models to include other form inputs. 

The API uses *TOKENS* not Sessions to store recent acitivity. Thanks to *djangorest_framework.authtoken* module, the token table is created in the database, and a string of values is created each time a new user is created. It is used when trying to refer to the current logged in user. 


## Requests Accepted 

*GET* and *POST* requests are accepted only, for now. 

## JSON Format

The format for the JSON key and value is as:

<code>
` {
    "email": "youremailexample@gmail.com",
    "fullname": "Jane Doe"
} `
</code>

## URL For Consumption

The API is hosted on Railway. Use this link:

*authenticationapidrf-production.up.railway.app/*



