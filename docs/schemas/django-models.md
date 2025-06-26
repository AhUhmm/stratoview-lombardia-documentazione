---
title: Django Models
sidebar_position: 3
---

# Django Models

## Model Files

📥 **Download Model Files:**

- [Django Models Python](/schemas/django/django-models.py)

## Implementation Example

```python
# From django-models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=10,
        choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'Customer')]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
```
