import { AngularFireList, AngularFireDatabase } from "angularfire2/database";
import { Product } from "../objects/product";
import { DatabaseHandler } from "./databaseHandler";
import { Order } from "../objects/orders";

export class FirebaseHandler implements DatabaseHandler {
    
  //public data: AngularFireList<any[]>
  public name = 'firebase'
  private orders: Order[] = []
  private products: Product[] = []
  private productOutput = null

  getProducts(db, callback=null) {
    if (this.products.length > 0) {
        if (callback) callback()
        return this.products
    }
    let data = db.list('/')
    data.valueChanges().subscribe(res => {
      this.productOutput = res[res.length-1]
      //console.log('data from DATABASE')
      //console.log(products)
      for (let i in this.productOutput) {
        let item = this.productOutput[i]
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
      if (callback){
        callback()
      }
    })
    console.log('products')
    console.log(this.products)
    return this.products
  }

  getCategories(db, callback=null) {
    let categories = []
    let data = db.list('/')
    data.valueChanges().subscribe(res => {
      let products = res[res.length-1]
      //console.log('data from DATABASE')
      //console.log(products)
      for (let i in products) {
        let item = products[i]
        if (!item['name'] && item[0].name) {
          item = item[0]
        }
        for (let j in item['categories']) {
          let cat = item['categories'][j]
          if(!categories.includes(cat)) {
            categories.push(cat)
          }
        }
      }
      if (callback){
        callback()
      }
    })
    console.log(categories)
    return categories
  }
  
  addProduct(db, product: Product) {
    let data = db.list('/product')
    var id = 1
    if (this.products.length ==0) {
        this.getProducts(db)
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
    data.push([newp])
  }
  
  saveProduct(db, product: Product) {
    console.log('save product')
    console.log(product)
    let pathSuffix = ''
    if (typeof(this.productOutput[product.key][0]) !== 'undefined') {
        pathSuffix = '/0'
    }
    db.object('/product/' + product.key + pathSuffix).update({
      name: product.name,
      price: product.price_for_one,
      quantity: product.quantity,
      description: product.description,
      id: product.id,
      img_url: product.img_url,
      categories: product.categories
    })
  }
  
  getOrders(db, callback=null) {
    if (this.orders.length > 0) {
        if (callback) callback()
        return this.orders
    }
    let data = db.list('/')
    console.log('data from DATABASE orders')
    console.log(data)
    var id = 0
    data.valueChanges().subscribe(res => {
        let orders = res[res.length-2]
        console.log('result:')
        console.log(orders)
        for (let i in orders) {
            let item = orders[i]
            if (item['address'] == null) {
            item = item[0]
            if (item['address'] == null) continue
            }
            //console.log('item')
            //console.log(item)
            let order: Order = new Order()
            order.address = item['address']
            order.products = item['products']
            order.totalPrice = item['totalPrice']
            order.status = item['status']
            order.id = item['id']
            order.key = i
            this.orders.push(order)
        }
        if (callback) {
            callback()
        }
    })
    return this.orders
  }
  
  finalizeOrder(db, order: Order) {
    console.log('db handler finalize order ')
    console.log(order)
    db.object('/order/' + order.key).update(order)
  }

  addOrder(db, products, address, callback) {
    console.log('firebase add order')
    var id = 1
    if (this.orders.length ==0) {
        this.getOrders(db)
    }
    id = this.orders.length + 1
    
    let totalPrice = 0
    for (let i in products) {
    let p = products[i]
    totalPrice += p.total_price
    }
    let data = db.list('/order')
    let date = new Date().toDateString()
    data.push([{
    products: products,
    address: address,
    totalPrice: totalPrice,
    date: date,
    id: id,
    status: 'waiting'}]).then(callback)
  }

}