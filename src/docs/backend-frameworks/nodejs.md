---
title: "Nodejs"
---

NodeJs

1. Node.js Basics
* What is Node.js? - A JavaScript runtime built on Chrome's V8 engine. Event-driven, non-blocking I/O model, single-threaded. Uses libuv for async operations.
* Why use Node.js? - High performance, handles concurrent connections (non-blocking I/O), rich NPM ecosystem, full-stack JS support.
* Key Features: Asynchronous/Event-driven, single-threaded with worker threads, modules for modularity.

2. Event Loop & Asynchronous Programming
* Event Loop Phases:
    1. Timers Phase (setTimeout, setInterval)
    2. I/O Callbacks (I/O operations, database queries)
    3. Idle/Prepare (Internal operations)
    4. Poll (Handles new I/O events)
    5. Check (Immediate callbacks like setImmediate())
    6. Close Callbacks (Cleanup like socket.on('close'))
* setTimeout(fn, 0): Executes in Timers phase
* setImmediate(fn): Executes in Check phase
* process.nextTick(fn): Executes BEFORE next event loop iteration

3. Node.js Modules & NPM
* CommonJS (require) vs ES Modules (import)
* const fs = require('fs');  // CommonJS
* import fs from 'fs';       // ES Modules (requires "type": "module" in package.json)
* Creating Custom Modules:
    // math.js
    module.exports.add = (a, b) => a + b;
    // app.js
    const { add } = require('./math');
    console.log(add(2, 3)); // 5
* NPM Commands: npm init -y, npm install express, npm update, npm list, npm uninstall <pkg>

4. File System (fs) Module
fs.readFile('file.txt', 'utf8', (err, data) => { ... });
fs.writeFile('output.txt', 'Hello Node.js!', err => { ... });

5. Streams and Buffers
* Types: Readable (fs.createReadStream), Writable (fs.createWriteStream), Duplex (TCP Sockets), Transform (zlib.createGzip)
* const readStream = fs.createReadStream('input.txt', 'utf8');
* readStream.on('data', chunk => { console.log('Received chunk:', chunk); });

6. HTTP & Express.js
* Simple HTTP Server:
    const http = require('http');
    const server = http.createServer((req, res) => {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello World');
    });
    server.listen(3000);
* Express Basics:
    const express = require('express');
    const app = express();
    app.get('/', (req, res) => res.send('Hello, Express!'));
    app.listen(3000);

7. Middleware in Express.js
* Types: Application-level (app.use()), Router-level (router.use()), Built-in (express.json()), Error-handling
* Custom Middleware: app.use((req, res, next) => { console.log(`${req.method} ${req.url}`); next(); });

8. Working with Databases
* MongoDB (Mongoose):
    const mongoose = require('mongoose');
    mongoose.connect('mongodb://localhost:27017/test');
    const User = mongoose.model('User', new mongoose.Schema({ name: String, age: Number }));
    User.create({ name: 'Alice', age: 25 });
* MySQL (mysql2):
    const db = mysql.createConnection({ host: 'localhost', user: 'root', database: 'test' });
    db.query('SELECT * FROM users', (err, results) => console.log(results));

9. Authentication with JWT
const token = jwt.sign({ userId: 123 }, 'secretkey', { expiresIn: '1h' });
jwt.verify(token, 'secretkey', (err, decoded) => { ... });

10. Error Handling
* Try-Catch for Async/Await:
    async function fetchData() {
      try { const data = await someAsyncFunction(); }
      catch (error) { console.error(error); }
    }
* Error Handling Middleware:
    app.use((err, req, res, next) => { res.status(500).send('Something went wrong!'); });

11. Worker Threads (CPU-intensive tasks)
const { Worker } = require('worker_threads');
const worker = new Worker('./worker.js');
worker.on('message', msg => console.log('Message from worker:', msg));

12. Deployment & Performance Optimization
* Use pm2 for process management
* Enable Gzip compression (compression package)
* Implement clustering (cluster module)
* Use caching (Redis, Node.js LRU Cache)
