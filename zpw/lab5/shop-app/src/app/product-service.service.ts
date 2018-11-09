import { Injectable } from '@angular/core';
import { Product } from './objects/product'
import { products } from './objects/fake_products'

@Injectable({
  providedIn: 'root'
})
export class ProductServiceService {

  public products: Product[] = products
  constructor() { }

  getProducts() {
    return this.products
  }

  getProduct() {
    return 0
  }

  addProduct(product: Product) {
    this.products.push(product)
  }

  deleteProduct(id: number) {
    /*for (let p of this.products) {
      if (id == p.id) {
        console.log('deleting ' + p.name)
        const index:number = this.products.indexOf(p)
        if (index > -1) {
          this.products.splice(index, 1)
        }
      }
    }*/
    for (let i=0 ; i<this.products.length ; ++i) {
      if (this.products[i].id == id) {
        this.products.splice(i, 1)
      }
    }
  }

}
