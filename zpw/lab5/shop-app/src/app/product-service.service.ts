import { Injectable } from '@angular/core';
import { Product } from './objects/product'
import { DbserviceService } from './dbservice.service';

@Injectable({
  providedIn: 'root'
})
export class ProductServiceService {

  public products: Product[] = []
  public categories = []

  constructor(private dbservice: DbserviceService) {
    //this.getProducts()
    this.getCategories()
  }

  getProducts(callback=null) {
    this.products = this.dbservice.getProducts(callback)
    return this.products
  }

  getCategories() {
    this.categories = this.dbservice.getCategories()
    console.log('categories')
    console.log(this.categories)
    return this.categories
  }

  addProduct(product: Product) {
    this.dbservice.addProduct(product)
  }

  updateProduct(id, field, value) {
    let fields = ['name', 'quantity', 'price_for_one', 'description', 'img_url', 'categories']
    if (!fields.includes(field)) {
      return
    }
    for (let i in this.products) {
      let p = this.products[i]
      if (p.id == id) {
        if (field == 'categories') {
          p[field] = (''+value).split(',')
        } else {
          p[field] = value
        }
      }
    }
  }

  performOrder(productsOfOrder) {
    console.log('perform order')
    let newQ = -1
    let newQs = []
    console.log('products of orer ')
    console.log(productsOfOrder)
    for(let i in productsOfOrder) {
      let poo = productsOfOrder[i]
      console.log('check with')
      console.log(this.products.slice())
      console.log(this.products.length)
      for (let j = 0 ; j<this.products.length ; ++j) {
        console.log('check '+this.products[j].id +' == '+ poo.id)
        if (this.products[j].id == poo.id) {
          console.log('update newq ['+ poo.id +']' + this.products[j].quantity +' - '+ poo.quantity )
          newQ = this.products[j].quantity - poo.quantity
        }
      }
      //this.updateProduct(p.id, 'quantity', newQ)
      newQs.push({id: poo.id, newq: newQ})
    }
    // check if all newq are positive
    for (var i in newQs) {
      let nq = newQs[i]
      if (nq['newq'] < 0) {
        console.log('no products, break')
        console.log(newQs)
        console.log(nq)
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
        this.dbservice.saveProduct(p)
      }
    }
  }

}
