import { Injectable } from '@angular/core';
import { Product } from './objects/product'
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';

@Injectable({
  providedIn: 'root'
})
export class ProductServiceService {

  public data: AngularFireList<any[]>
  public products: Product[] = []
  public categories = []

  constructor(private db: AngularFireDatabase) {
    this.getProducts()
  }

  getProducts(callback=null) {
    if (this.products.length > 0) {
      return this.products
    }
    this.data = this.db.list('/')
    this.data.valueChanges().subscribe(res => {
      let products = res[res.length-1]
      //console.log('data from DATABASE')
      //console.log(products)
      for (let i in products) {
        let item = products[i]
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
          if(!this.categories.includes(cat)) {
            this.categories.push(cat)
          }
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
    console.log(this.products)
    return this.products
  }

  getCategories() {
    return this.categories
  }

  getProduct() {
    return 0
  }

  addProduct(product: Product) {
    let newp = new Product()
    newp.name = product.name
    newp.description = product.description
    newp.img_url = product.img_url
    newp.price = product.price_for_one
    newp.quantity = product.quantity
    newp.categories = product.categories
    newp.id = this.products.length
    this.data.push([newp])
  }

  deleteProduct(id: number) {
    for (let i=0 ; i<this.products.length ; ++i) {
      if (this.products[i].id == id) {
        this.products.splice(i, 1)
      }
    }
  }

  updateProduct(id, field, value) {
    let fields = ['name', 'quantity', 'price_for_one', 'description', 'img_url', 'categories']
    if (!fields.includes(field)) {
      return
    }
    for (let i in this.products) {
      let p = this.products[i]
      if (p.id == id) {
        p[field] = value
      }
    }
  }

  performOrder(products) {
    console.log('perform order')
    let newQ = -1
    let newQs = []
    for(let i in products) {
      let p = products[i]
      for (let j in this.products) {
        if (this.products[j].id == p.id) {
          newQ = this.products[j].quantity - p.quantity
        }
      }
      //this.updateProduct(p.id, 'quantity', newQ)
      newQs.push({id: p.id, newq: newQ})
    }
    // check if all newq are positive
    for (var i in newQs) {
      let nq = newQs[i]
      if (nq['newq'] < 0) {
        return false
      }
    }
    // all ok
    for (var i in newQs) {
      let nq = newQs[i]
      console.log('performOrder:update product')
      console.log(nq)
      this.updateProduct(nq['id'], 'quantity', nq['newq'])
      this.saveProduct(nq['id'])
    }
    return true
  }

  saveProduct(id) {
    for (let i in this.products) {
      let p = this.products[i]
      if (p.id == id) {
        // save to DB todo
        console.log('save product')
        console.log(p)
        this.db.object('/product/' + p.key).update({
          name: p.name,
          price: p.price_for_one,
          quantity: p.quantity,
          description: p.description,
          id: p.id,
          img_url: p.img_url,
        })
      }
    }
  }

}
