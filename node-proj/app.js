const http = require('http');

// const hostname = '127.0.0.1';
const hostname = '0.0.0.0';
const port = 3000;

const Blinkt = require('node-blinkt'),
    leds = new Blinkt();

const server = http.createServer((req, res) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello World\n');
    });

server.listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`);
        leds.setup();
        leds.clearAll();
        leds.setAllPixels(0, 156, 0, 0.1);
        leds.sendUpdate();

    });

