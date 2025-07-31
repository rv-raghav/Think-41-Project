const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./products.db');

db.all("PRAGMA table_info(products)", [], (err, rows) => {
  if (err) {
    console.error("Error fetching columns:", err);
  } else {
    console.log("Table columns:");
    rows.forEach(col => console.log(col.name));
  }
  db.close();
});
