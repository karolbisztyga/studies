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
var bodyParser = require('body-parser')
var app = express();
const mongodb = require('mongodb').MongoClient
var db = null
var ObjectID = require('mongodb').ObjectID;

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

app.use(bodyParser.json())

mongodb.connect('mongodb://travis:asd123@ds231460.mlab.com:31460/zpwlab', (err, database) => {
    log('mongo connect')
    if (err) {
        log('mongo connect error', 'fail')
        log(err, raw)
        return
    }
    log('mongo connect success', 'succ')
    db = database.db('zpwlab')
    //log(db, raw)
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
app.post('/product', function (req, res) {
    log('adding product')
    log(req.body, raw)
    // adding to database
    db.collection("products").insertOne(req.body, function(err, res2) {
        if (err) {
            log('error inserting object', 'err')
            log(err, raw)
            res.send(JSON.stringify('object not inserted, error occured'))
            return
        }
        log('object inserted', 'succ')
        res.send(JSON.stringify('object inserted'))
    });

})

// update product
app.put('/product/:id', function (req, res) {
    log('updating product')
    let id = req.params['id']
    log('product id ' + id)
    let query = { _id: ObjectID(id) }
    let newValues = {$set: req.body}
    log(query, raw)
    log(newValues, raw)
    db.collection("products").updateOne(query, newValues, function(err, res2) {
        if (err) {
            log('error updating object', 'err')
            log(err, raw)
            res.send(JSON.stringify('object not updated, error occured'))
            return
        }
        log('object updated', 'succ')
        res.send(JSON.stringify('object updated'))
    });
})

// get orders
app.get('/orders', function (req, res) {
    log('obtaining orders')
    if (!db) {
        log('database undefined', 'err')
        return
    }
    let cursor = db.collection('orders').find()
    cursor.toArray(function(err, results) {
        if (err) {
            log(err, 'err')
            return
        }
        res.send(JSON.stringify(results))
        return
    })
})

// finalize orders
app.put('/order/:id', function (req, res) {
    log('finalizing order')
    let id = req.params['id']
    log('order id '+ id)
    let query = { _id: ObjectID(id) }
    let newValues = {$set: req.body}
    log(query, raw)
    log(newValues, raw)
    db.collection("orders").updateOne(query, newValues, function(err, res2) {
        if (err) {
            log('error updating object', 'err')
            log(err, raw)
            res.send(JSON.stringify('object not updated, error occured'))
            return
        }
        log('object updated', 'succ')
        res.send(JSON.stringify('object updated'))
    });
})

// add order
app.post('/order', function (req, res) {
    log('adding product')
    log(req.body, raw)
    // adding to database
    db.collection("orders").insertOne(req.body, function(err, res2) {
        if (err) {
            log('error inserting object', 'err')
            log(err, raw)
            res.send(JSON.stringify('object not inserted, error occured'))
            return
        }
        log('object inserted', 'succ')
        res.send(JSON.stringify('object inserted'))
    });

})
