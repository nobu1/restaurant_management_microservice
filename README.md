# Restaurant Management Microservice

A modular, microservices-based restaurant management system. This project demonstrates loosely-coupled services.

---

## Table of Contents

- [Restaurant Management Microservice](#restaurant-management-microservice)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Microservices](#microservices)

---

## Features
- **Admin Management:** Show restaurant, customers, reservations, and coupons data.
- **Coupon Management:** Add, update coupon items.
- **Customer Management:** Register and manage customer profiles.
- **Restaurant Management:** Add, update restaurants.
---

## Architecture

This project follows a microservices architecture. Each core feature is implemented as an independent service, allowing for easier scaling, deployment, and maintenance.

Services communicate via ZeroMQ.

---

## Microservices

| Service             | Description                                 |  
|---------------------|---------------------------------------------|  
| Reservation Service | Show reservation data with 5 customers      |
| Customer Service    | Show customer age profiles with pie chart   |  
| Coupon Service      | Show coupon data with bar chart             |  
| Restaurant Service  | Show restaurant status with pie chart       |  
  
> **Note:** Please refer to each service's directory for specific implementation details.
