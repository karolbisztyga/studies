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
