/**
 * operations to implement:
 *      get products
 *      get categories
 *      add product
 *      update product
 *      get orers
 *      finalize order
 *      add order
 * 
 */

// helper functions and consts
const raw = 'raw'
var log = function(info, type='msg')
{
    if (type == 'raw') {
        console.log(info)
        return
    }
    let sign = '*'
    if (type == 'err') sign = '!'
    if (type == 'fail') sign = '-'
    if (type == 'succ') sign = '+'
    console.log('['+ sign +'] ' + info)
}
 
var express = require('express');
var app = express();
const mongodb = require('mongodb').MongoClient
var db = null

// Add headers
app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4200');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});

mongodb.connect('mongodb://travis:asd123@ds231460.mlab.com:31460/zpwlab', (err, database) => {
    log('mongo connect')
    if (err) {
        log('mongo connect error', 'fail')
        log(err, raw)
        return
    }
    log('mongo connect success', 'succ')
    db = database.db('zpwlab')
    log(db, raw)
    var server = app.listen(5000, function () {
        var host = server.address().address
        var port = server.address().port
        log('app listening on http://' + host + ':' + port)
    });
})

app.get('/', function (req, res) {
    log('get /')
    res.send('Hello GET')
})

// get produts
app.get('/products', function (req, res) {
    log('obtaining products')
    if (!db) {
        log('database undefined', 'err')
        return
    }
    let cursor = db.collection('products').find()
    cursor.toArray(function(err, results) {
        if (err) {
            log(err, 'err')
            return
        }
        res.send(JSON.stringify(results))
        return
    })
})

// get categories
app.get('/categories', function (req, res) {
    log('obtaining categories')
    if (!db) {
        log('database undefined', 'err')
        return
    }
    let categories = []
    let cursor = db.collection('products').find()
    cursor.toArray(function(err, results) {
        if (err) {
            log(err, 'err')
            return
        }
        for (var i in results) {
            let prod = results[i]
            let cats = prod['categories']
            for (let j in cats) {
                let cat = cats[j]
                if (!categories.includes(cat)) {
                    categories.push(cat)
                }
            }
        }
        res.send(JSON.stringify(categories))
        return
    })
})

// add product
app.put('/product', function (req, res) {
    log('adding product')
})

// update product
app.post('/product', function (req, res) {
    log('updating product')
})

// get orders
app.get('/orders', function (req, res) {
    log('obtaining orders')
})

// finalize orders
app.post('/order', function (req, res) {
    log('finalizing order')
})

// add order
app.put('/order', function (req, res) {
    log('adding order')
})


/*
app.post('/', function (req, res) {
    console.log("Otrzymano żądanie POST dla strony głównej");
    res.send('Hello POST');
})
app.delete('/usun', function (req, res) {
    console.log("Otrzymano żądanie DELETE dla strony /usun");
    res.send('Hello DELETE');
})
app.put('/user_list', function (req, res) {
    console.log("Otrzymano żądanie PUTdla strony /user_list");
    res.send('Lista użytkowników');
})
app.get('/ab*cd', function(req, res) { // wzorzec strony: abcd, abxcd, ab123cd, ...
    console.log("Otrzymano żądanie GET dla strony /ab*cd");
    res.send('Wzorzec strony dopasowany');
})
*/