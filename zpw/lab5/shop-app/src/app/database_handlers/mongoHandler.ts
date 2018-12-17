import { DatabaseHandler } from "./databaseHandler";
import { Product } from "../objects/product";
import { Order } from "../objects/orders";
import { RequestOptions, Headers } from '@angular/http';

export class MongoHandler implements DatabaseHandler {

    public name = 'mongo'
    //private base_url = 'http://localhost:5000/'
    private base_url = 'https://zpwlab.herokuapp.com/'
    private orders: Order[] = []
    private products: Product[] = []

    constructor() {}

    getProducts(http, callback=null) {
        console.log('mongo getProducts()')
        let cpHeaders = new Headers({ 'Content-Type': 'application/json' })
        let options = new RequestOptions({ headers: cpHeaders })
        let url = 'products'
        http.get(this.base_url + url, options).subscribe(res => {
            let productOutput = JSON.parse(res['_body'])
            for (let i in productOutput) {
                let item = productOutput[i]
                if (!item['name'] && item[0].name) {
                    item = item[0]
                }
                //console.log('item')
                //console.log(item)
                let product: Product = new Product()
                product.name = item['name']
                product.quantity = item['quantity']
                product.categories = []
                for (let j in item['categories']) {
                    let cat = item['categories'][j]
                    product.categories.push(cat)
                }
                product.description = item['description']
                product.img_url = item['img_url']
                product.price_for_one = item['price']
                product.id = item['id']
                product.key = item['_id']
                this.products.push(product)
            }
            console.log('DATA FROM MONGODB products')
            console.log(this.products)
            if (callback) {
                callback()
            }
        })

        return this.products
    }

    getCategories(http, callback=null) {
        console.log('mongo getCategories()')
        let categories = []
        let headers = new Headers({ 'Content-Type': 'application/json' })
        let options = new RequestOptions({ headers: headers })
        let url = 'categories'
        http.get(this.base_url + url, options).subscribe(res => {
            let catOutput = JSON.parse(res['_body'])
            for (let i in catOutput) {
                categories.push(catOutput[i])
            }
        })
        return categories
    }
    
    addProduct(http, product: Product, callback=null) {
        console.log('mongo addProduct()')
        
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers })
        let url = 'product'
        
        var id = 1
        if (this.products.length ==0) {
            this.getProducts(http)
        }
        id = this.products.length + 1
        let newp = new Product()
        newp.name = product.name
        newp.description = product.description
        newp.img_url = product.img_url
        newp.price = product.price_for_one
        newp.quantity = product.quantity
        newp.categories = product.categories
        newp.id = id
        console.log(newp)
        
        let result = http.post(this.base_url + url, newp, options).subscribe(res => {
            console.log('put result')
            console.log(res)
            if (callback) callback()
        })
    }
    
    saveProduct(http, product: Product, callback=null) {
        console.log('mongo saveProduct()')
        console.log(product)
        
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers })
        let newp = {
            name: product.name,
            price: product.price_for_one,
            quantity: product.quantity,
            description: product.description,
            id: product.id,
            img_url: product.img_url,
            categories: product.categories
        }
        let url = 'product/' + product.key
        let result = http.put(this.base_url + url, newp, options).subscribe(res => {
            console.log('put result')
            console.log(res)
            if(callback) callback()
        })
    }
    
    getOrders(http, callback=null) {
        console.log('mongo getOrders()')
        let cpHeaders = new Headers({ 'Content-Type': 'application/json' })
        let options = new RequestOptions({ headers: cpHeaders })
        let url = 'orders'
        http.get(this.base_url + url, options).subscribe(res => {
            let orders = JSON.parse(res['_body'])
            console.log('result:')
            console.log(orders)
            for (let i in orders) {
                let item = orders[i]
                if (item['address'] == null) {
                item = item[0]
                if (item['address'] == null) continue
                }
                console.log('item')
                console.log(item)
                let order: Order = new Order()
                order.address = item['address']
                order.products = item['products']
                order.totalPrice = item['totalPrice']
                order.status = item['status']
                order.id = item['id']
                order.key = item['_id']
                this.orders.push(order)
            }
            console.log('DATA FROM MONGODB orders')
            console.log(this.orders)
            if (callback) {
                callback()
            }
        })
        return this.orders
    }
    
    finalizeOrder(http, order: Order, callback=null) {
        console.log('mongo finalizeOrder()')
        console.log(order)

        let headers = new Headers({ 'Content-Type': 'application/json' })
        let options = new RequestOptions({ headers: headers })
        let url = 'order/' + order.key
        let newo = {
            status: 'done'
        }
        console.log('url:' + url)
        let result = http.put(this.base_url + url, newo, options).subscribe(res => {
            console.log('put result')
            console.log(res)
            if (callback) callback()
        })

        return null
    }

    addOrder(http, products, address, callback) {
        console.log('mongo addOrder()')
        var id = 1
        var that = this
        let add = function() {
            id = that.orders.length + 1
            
            let totalPrice = 0
            for (let i in products) {
                let p = products[i]
                totalPrice += p.total_price
            }
    
            let date = new Date().toDateString()
            let newo = {
                products: products,
                address: address,
                totalPrice: totalPrice,
                date: date,
                id: id,
                status: 'waiting'
            }
    
            let headers = new Headers({ 'Content-Type': 'application/json' })
            let options = new RequestOptions({ headers: headers })
            let url = 'order'
            let result = http.post(that.base_url + url, newo, options).subscribe(res => {
                console.log('post result')
                console.log(res)
                callback()
            })
        }

        if (this.orders.length == 0) {
            this.getOrders(http, add)
        } else {
            add()
        }
    }

}