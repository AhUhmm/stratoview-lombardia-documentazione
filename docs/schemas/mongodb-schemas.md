---
title: MongoDB Schemas
sidebar_position: 2
---

# MongoDB Schemas

## Schema Files

📥 **Download Schema Files:**

- [MongoDB Schema JavaScript](/schemas/mongodb/mongodb-schema.js)
- [Taxonomy Store JSON](/schemas/taxonomy-store.json)

## Collections Overview

### User Collection

```javascript
// From mongodb-schema.js
const UserSchema = {
  _id: "ObjectId",
  username: "string",
  email: "string",
  userType: {
    type: "string",
    enum: ["ADMIN", "CUSTOMER"],
  },
  createdAt: "ISODate",
  lastLogin: "ISODate",
};
```
