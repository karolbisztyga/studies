import { Component, OnInit } from '@angular/core';
import { BasketServiceService } from '../basket-service.service';
import { Product } from '../objects/product';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.scss']
})
export class BasketComponent implements OnInit {
  public products: Product[]
  public price: number
  constructor(private basketService: BasketServiceService) {
  }

  ngOnInit() {
    this.products = this.basketService.basketProducts
    this.price = this.basketService.getTotalPrice()
    console.log('price ' + this.price)
    console.log(this.basketService.getProducts())
  }

  remove(event, product) {
    console.log('remove ' + product.id)
    this.basketService.deleteProduct(product.id)
    this.updatePrice()
  }

  increaseQuantity(event, product) {
    console.log('increase quantity of ' + product.id)
    this.basketService.increaseQuantity(product.id)
    this.updatePrice()
  }

  decreaseQuantity(event, product) {
    console.log('decrease quantity of ' + product.id)
    this.basketService.decreaseQuantity(product.id)
    this.updatePrice()
  }

  updatePrice() {
    this.price = this.basketService.getTotalPrice()
  }

  productsNotEmpty() {
    return (this.products.length > 0)
  }

}
