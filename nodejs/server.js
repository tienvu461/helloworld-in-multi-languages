'use strict';

const express = require('express');
const fs = require('fs');

// Constants
const PORT = 3000;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
    fs.readFile('health.json', (e, data) => {
        if (e) throw e;
        let health = JSON.parse(data);
        res.setHeader('content-type', 'application/json');
        res.send(health);
    });
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
