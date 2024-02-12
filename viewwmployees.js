const { createPool } = require('mysql');

const pool = createPool({
    host: "localhost",
    user: "root",
    password: "neeraj",
    database: "employees",
    connectionLimit: 10
});
