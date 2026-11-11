# Inventory Management System

A CLI-based Inventory Management System built using pure Object-Oriented Python.

## Domain

Warehouse / Medical Product Distributor

## Project Goal

This project manages:

- Suppliers
- Customers
- Medical products
- General products
- Inventory stock
- Customer orders
- Sales reports
- Expiry alerts

## CLI Menu

INVENTORY MANAGEMENT SYSTEM
----------------------------------------
1. View Inventory
2. Search Product
3. View Inventory Summary Report
4. View Expiry Alert Report
5. Place Order
6. Exit

## Folder Structure

```text
inventory_management/
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── supplier.py
│   ├── customer.py
│   ├── product.py
│   ├── medical_product.py
│   ├── general_product.py
│   ├── order_item.py
│   ├── order.py
│   └── inventory.py
│
├── reports/
│   └── report.py
│
├── main.py
└── README.md