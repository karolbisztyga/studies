import { FirebaseHandler } from "./firebaseHandler";
import { MongoHandler } from "./mongoHandler";
import { Product } from "../objects/product";
import { Order } from "../objects/orders";

export interface DatabaseHandler {

    name:string
    getProducts(tool, callback)
    getCategories(tool, callback)
    addProduct(tool, product: Product)
    saveProduct(tool, product: Product)
    getOrders(tool, callback)
    finalizeOrder(tool, order: Order)
    addOrder(tool, products, address, callback)

}