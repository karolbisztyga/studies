import { FirebaseHandler } from "./firebaseHandler";
import { MongoHandler } from "./mongoHandler";
import { Product } from "../objects/product";
import { Order } from "../objects/orders";

export interface DatabaseHandler {

    name:string
    getProducts(db, callback)
    getCategories(db, callback)
    addProduct(db, product: Product)
    saveProduct(db, product: Product)
    getOrders(db, callback)
    finalizeOrder(db, order: Order)
    addOrder(db, products, address, callback)

}