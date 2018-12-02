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
    this.data = this.db.list('/product')
    console.log('data from DATABASE')
    this.data.valueChanges().subscribe(res => {
      for (let i in res) {
        let item = res[i]
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
    })
    console.log(this.products)
  }

  getProducts() {
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
    newp.price_for_one = product.price_for_one
    newp.quantity = product.quantity
    newp.id = this.products[this.products.length-1].id + 1
    this.products.push(newp)
  }

  deleteProduct(id: number) {
    for (let i=0 ; i<this.products.length ; ++i) {
      if (this.products[i].id == id) {
        this.products.splice(i, 1)
      }
    }
  }

}
