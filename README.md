# Little lemon website

This project is based on the Meta Back-End Developer Professional Certificate Course 8(https://www.coursera.org/learn/back-end-developer-capstone?specialization=meta-back-end-developer). 

Table of Contents
=================

1. Installation
2. About
3. Features
4. Future developments


## 1. Installation
Virtualenv was used to manage all the dependencies into a virtual environment
Installing virtualenv:
```
pip install virtualenv
```
After cloning the project, use the following command to install all the dependencies:
```
pip install -r requirements.txt
```
Next step is to update the settings.py DATABASE section accordingly to your database preferences(MySQL, POSTGRESQL or SQLITE)

## 2. About

In this project, a website was developed for the owners of Little Lemon restaurant. The site consists of 5 pages:
1. Home -> main page;
2. About -> restaurant description;
3. Menu -> the menu available;
4. Book -> restaurant booking table;
5. Reservations -> all bookings.

## 3. Features

1. ModelForm -> Booking;
2. Model -> Menu;
3. APIs:
```
menu/
menu/<int:pk>
bookings/
```
4. Tests -> model and view tests;

## 4. Future developments

1. Split the Menu model into 2 models: Course(Starter, Main and Dessert) and Dish. Update the Menu page and the menu API endpoint to reflect this change;
2. Reservation page to be available only to the owner and staff of the restaurant;
