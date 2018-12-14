import { DatabaseHandler } from "./databaseHandler";
import { Product } from "../objects/product";
import { Order } from "../objects/orders";

export class MongoHandler implements DatabaseHandler {

    public name = 'mongo'

    getProducts(db, callback=null) {
        console.log('mongo getProducts()')
        return null
    }

    getCategories(db, callback=null) {
        console.log('mongo getCategories()')
        return null
    }
    
    addProduct(db, product: Product) {
        console.log('mongo addProduct()')
        return null
    }
    
    saveProduct(db, product: Product) {
        console.log('mongo saveProduct()')
        return null
    }
    
    getOrders(db, callback=null) {
        console.log('mongo getOrders()')
        return null
    }
    
    finalizeOrder(db, order: Order) {
        console.log('mongo finalizeOrder()')
        return null
    }

    addOrder(db, products, address, callback) {
        console.log('mongo addOrder()')
        return null
    }

}