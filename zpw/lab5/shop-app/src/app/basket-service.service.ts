import { Injectable } from '@angular/core';
import { Product } from './objects/product';
import { products } from './objects/fake_products';


@Injectable({
  providedIn: 'root'
})
export class BasketServiceService {

  public basketProducts: Product[] = []
  public totalPrice = 0

  constructor() {
  }

  getTotalPrice() {
    console.log('basket service total price is ' + this.totalPrice)
    return this.totalPrice
  }

  productInBasket(id: number) {
    for(let i = 0; i < this.basketProducts.length; ++i) {
      let product = this.basketProducts[i]
      if (product.id == id) {
        console.log('product of id ' + id + ' is in the basket')
        return true
      }
    }
    return false
  }

  addProduct(productId: number) {
    console.log('basket add product')
    for(let i = 0; i < products.length; ++i) {
      let product = products[i]
      if (product.id == productId) {
        console.log(product)
        if (this.productInBasket(productId)) {
          this.increaseQuantity(productId)
          return
        }
        let newp = new Product()
        newp.name = product.name
        newp.description = product.description
        newp.img_url = product.img_url
        newp.price_for_one = product.price_for_one
        newp.quantity = 1
        newp.id = product.id
        this.basketProducts.push(newp)
        this.updatePrice()
        break;
      }
    }
    
  }

  getProducts() {
    return this.basketProducts
  }

  deleteProduct(id: number) {
    for (let i=0 ; i<this.basketProducts.length ; ++i) {
      if (this.basketProducts[i].id == id) {
        this.basketProducts.splice(i, 1)
        this.updatePrice()
      }
    }
  }

  increaseQuantity(id: number) {
    for (let i=0 ; i<this.basketProducts.length ; ++i) {
      if (this.basketProducts[i].id == id) {
        console.log('increasing qunatity of product of id ' + id)
        ++this.basketProducts[i].quantity;
        this.updatePrice()
      }
    }
  }

  decreaseQuantity(id: number) {
    for (let i=0 ; i<this.basketProducts.length ; ++i) {
      if (this.basketProducts[i].id == id) {
        console.log('decreasing qunatity of product of id ' + id)
        if(this.basketProducts[i].quantity > 1) {
          --this.basketProducts[i].quantity;
        } else {
          this.deleteProduct(id)
        }
        this.updatePrice()
      }
    }
  }

  updatePrice() {
    console.log('update price')
    this.totalPrice = 0
    for (let i=0 ; i<this.basketProducts.length ; ++i) {
      let product = this.basketProducts[i]
      console.log(product.price_for_one + ' * ' + product.quantity)
      this.totalPrice += product.price_for_one * product.quantity
    }
    console.log('basket service new price ' + this.totalPrice)
    for (let i = 0; i < this.basketProducts.length; ++i) {
      let product = this.basketProducts[i];
      product.total_price = product.price_for_one * product.quantity;
    }
  }

}
