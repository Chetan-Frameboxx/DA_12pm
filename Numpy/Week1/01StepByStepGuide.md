# Week 1 Backend — Step-by-step Guide

---

## Prerequisites

* Node.js and npm installed (Node 14+ recommended). Check with:

  ```bash
  node -v
  npm -v
  ```

* MongoDB running locally (default `mongodb://127.0.0.1:27017`) **or** a MongoDB Atlas connection string.

* Optional but helpful: `nodemon` installed as dev dependency (already in package.json).

* Postman (or curl) for testing endpoints.

---

## High-level plan (what we'll do)

1. Create project folder and files.
2. Add `package.json` (you have one provided).
3. Install dependencies.
4. Implement database connection in `config/db.js`.
5. Create `Product` Mongoose model.
6. Implement routes in `routes/productRoutes.js`.
7. Create `server.js` to wire everything and start the Express server.
8. Start MongoDB, run the server, and test endpoints with Postman.
9. (Optional) Improve error handling, validation, environment variables.

---

## Step 1 — Create the project folder and structure

Open a terminal and run:

```bash
mkdir week1-backend
cd week1-backend

# create folders
mkdir config models routes

# create files (use your editor or these commands)
# on Unix/macOS
touch package.json server.js config/db.js models/Product.js routes/productRoutes.js
```

> You already have the `package.json` content. If you prefer, paste that content into `package.json` instead of `npm init`.

---

## Step 2 — Install dependencies

If you pasted the `package.json`, install dependencies with:

```bash
npm install
```

If you want to initialize and install manually:

```bash
npm init -y
npm install express mongoose cors
npm install --save-dev nodemon
```

`nodemon` allows auto-restarts during development. Use `npm run dev` (from package.json) to start in dev mode.

---

## Step 3 — Start MongoDB

**Local MongoDB:**

* If you have MongoDB installed locally, start it (platform-specific). On many systems:

  ```bash
  # macOS using Homebrew
  brew services start mongodb-community

  # Linux (systemd)
  sudo systemctl start mongod
  ```

* Confirm connection (optional):

  ```bash
  mongo --eval "db.adminCommand('ping')"
  ```

**MongoDB Atlas:**

* If you use Atlas, create a cluster and copy the connection string. Replace the URI in `config/db.js` or, better, use an environment variable.

---

## Step 4 — Add the DB connection (`config/db.js`)

Use the code you provided. Save the file as `config/db.js`.

```js
const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    await mongoose.connect("mongodb://127.0.0.1:27017/week1db");
    console.log("MongoDB Connected");
  } catch (error) {
    console.error("DB Connection Error", error);
    process.exit(1);
  }
};

module.exports = connectDB;
```

**Tip:** For production or sharing with students, use `process.env.MONGO_URI` and a `.env` file. (See Optional Improvements section.)

---

## Step 5 — Create the Product model (`models/Product.js`)

Put this content in `models/Product.js`:

```js
const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  price: { type: Number, required: true },
  category: { type: String, required: true },
});

module.exports = mongoose.model('Product', productSchema);
```

This defines a simple schema with three required fields.

---

## Step 6 — Create routes (`routes/productRoutes.js`)

Save the following code to `routes/productRoutes.js` (this is the code you provided). It exposes four endpoints for CRUD operations.

```js
const express = require("express");
const router = express.Router();
const Product = require("../models/Product");

// CREATE
router.post('/', async (req, res) => {
  const product = await Product.create(req.body);
  res.json(product);
});

// READ
router.get('/', async (req, res) => {
  const products = await Product.find();
  res.json(products);
});

// UPDATE
router.put('/:id', async (req, res) => {
  const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(product);
});

// DELETE
router.delete('/:id', async (req, res) => {
  await Product.findByIdAndDelete(req.params.id);
  res.json({ message: "Product removed" });
});

module.exports = router;
```

**Important notes for faculty to demo:**

* The code above doesn’t handle errors or missing resources. In the demo, show what happens when invalid payloads or IDs are sent.
* We'll add robust error handling in the optional improvements section.

---

## Step 7 — Wire up Express (`server.js`)

Save this content to `server.js`:

```js
const express = require("express");
const cors = require("cors");
const connectDB = require("./config/db");
const productRoutes = require("./routes/productRoutes");

const app = express();
connectDB();

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send("API is running...");
});

app.use("/api/products", productRoutes);

app.listen(5000, () => console.log("Server running on port 5000"));
```

Start server in dev mode:

```bash
npm run dev
```

You should see output like: `MongoDB Connected` and `Server running on port 5000`.

---

## Step 8 — Test using Postman (or curl)

Base URL:

```
http://localhost:5000/api/products
```

### 1) Create (POST)

* **URL:** `POST /api/products`
* **Headers:** `Content-Type: application/json`
* **Body (raw JSON):**

```json
{
  "name": "Sample Product",
  "price": 199.99,
  "category": "electronics"
}
```

* **Expected:** Response body is the newly created product object (includes `_id`).

**curl example:**

```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Sample Product","price":199.99,"category":"electronics"}'
```

### 2) Read (GET all)

* **URL:** `GET /api/products`
* **Expected:** Array of product objects.

**curl:**

```bash
curl http://localhost:5000/api/products
```

### 3) Update (PUT)

* **URL:** `PUT /api/products/:id`
* **Body:** partial or full object to update (JSON). Example:

```json
{ "price": 179.99 }
```

* **Expected:** Response body is the updated product document.

**curl:**

```bash
curl -X PUT http://localhost:5000/api/products/<ID> \
  -H "Content-Type: application/json" \
  -d '{"price":179.99}'
```

### 4) Delete (DELETE)

* **URL:** `DELETE /api/products/:id`
* **Expected:** `{ message: "Product removed" }`

**curl:**

```bash
curl -X DELETE http://localhost:5000/api/products/<ID>
```

---

## Step 9 — Faculty demonstration checklist

When demonstrating to students, cover these points:

* Show how to start MongoDB and the Express server.
* Demonstrate each CRUD endpoint in Postman (show request and response). Use real examples (create 2–3 products).
* Show `GET /api/products` returning an array with created items.
* Show updating a product and explain `new: true` in `findByIdAndUpdate`.
* Show deleting a product and then `GET` to confirm removal.
* Intentionally send a bad request or malformed ID to show what errors look like with the current code.
* Explain how to inspect logs in the terminal and where to add `console.log` statements.

---

## Optional improvements (good teaching points)

1. **Add try/catch + proper error handling** in each route. Return appropriate HTTP status codes (e.g., 201 for create, 404 when item not found, 400 for bad request, 500 for server error).

2. **Validation**: Use a validation library (Joi or Mongoose validators) and return helpful messages.

3. **Use environment variables** (`dotenv`) to store `MONGO_URI` and `PORT`.

4. **Centralized error middleware**: Add a middleware to catch async errors and standardize responses.

5. **Seed script**: Create a small script that seeds sample products for quick demos.

6. **Logging**: Use `morgan` for request logging during development.

7. **CORS configuration**: Restrict origins when moving to production.

8. **Explain REST conventions**: status codes, endpoint naming, idempotency of PUT vs PATCH.

---

### Quick example: safer CREATE route with error handling

```js
// inside routes/productRoutes.js
router.post('/', async (req, res) => {
  try {
    const { name, price, category } = req.body;
    if (!name || !price || !category) {
      return res.status(400).json({ message: 'All fields are required' });
    }
    const product = await Product.create({ name, price, category });
    return res.status(201).json(product);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: 'Server error' });
  }
});
```

---

## Wrap-up and suggested next class activity

* Homework: Students should extend the model to add `description`, `countInStock`, and `image` fields and update routes accordingly.
* Mini project: Build a small React frontend that lists products and allows create/update/delete using the API.

---

If you want, I can convert this guide into a printable PDF, or add code snippets with full files ready to download. Toggle any of the optional improvements and I will add the exact code changes here.
