const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");
const path = require("path");

const app = express();
const db = new sqlite3.Database("products.db");

app.use(cors());
app.use(express.json());

// Get all products
app.get("/api/products", (req, res) => {
  db.all("SELECT * FROM products", [], (err, rows) => {
    if (err) {
      console.error("DB error:", err);
      return res.status(500).json({ error: "Error retrieving products." });
    }
    res.json(rows);
  });
});

// Get product by ID
app.get("/api/products/:id", (req, res) => {
  const productId = req.params.id;
  console.log("Looking up product ID:", productId);

  db.get("SELECT * FROM products WHERE id = ?", [productId], (err, row) => {
    if (err) {
      console.error("DB error:", err);
      return res.status(500).json({ error: "Error retrieving product." });
    }

    if (!row) {
      return res.status(404).json({ error: "Product not found" });
    }

    res.json(row);
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
