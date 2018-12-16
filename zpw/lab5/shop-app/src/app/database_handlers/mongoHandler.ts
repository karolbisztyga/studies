import { DatabaseHandler } from "./databaseHandler";
import { Product } from "../objects/product";
import { Order } from "../objects/orders";
import { RequestOptions, Headers } from '@angular/http';

export class MongoHandler implements DatabaseHandler {

    public name = 'mongo'
    private base_url = 'http://localhost:5000/'
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
                product.key = i
                this.products.push(product)
            }
            console.log('DATA FROM MONGODB')
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
    
    addProduct(http, product: Product) {
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
        })
    }
    
    saveProduct(http, product: Product) {
        console.log('mongo saveProduct()')
        return null
    }
    
    getOrders(http, callback=null) {
        console.log('mongo getOrders()')
        return null
    }
    
    finalizeOrder(http, order: Order) {
        console.log('mongo finalizeOrder()')
        return null
    }

    addOrder(http, products, address, callback) {
        console.log('mongo addOrder()')
        return null
    }

}