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
  private currId: number = 0

  constructor(private db: AngularFireDatabase) {
    this.getProducts()
  }

  getProducts(callback=null) {
    if (this.products.length > 0) {
      return this.products
    }
    this.data = this.db.list('/product')
    console.log('data from DATABASE')
    this.data.valueChanges().subscribe(res => {
      for (let i in res) {
        let item = res[i]
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
        product.id = ++this.currId
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
    newp.id = this.products[this.products.length-1].id + 1
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
        // save to DB todo
      }
    }
  }

}
