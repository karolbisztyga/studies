import { Component, OnInit } from '@angular/core';
import { BasketServiceService } from '../basket-service.service';
import { Product } from '../objects/product';
import { Router } from '@angular/router';
import { OrderServiceService } from '../order-service.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss']
})
export class CheckoutComponent implements OnInit {
  public products: Product[]
  public price: number
  public address = ''
  public notes = ''
  public msg = ''

  constructor(
    private basketService: BasketServiceService,
    private router: Router,
    private orderService: OrderServiceService) {
  }

  ngOnInit() {
    this.products = this.basketService.basketProducts
    // if there are no products, redirect to /products
    if (this.products.length == 0) {
      this.router.navigateByUrl('/dashboard')
    }
    this.price = this.basketService.getTotalPrice()
  }

  updateInfo(key, value) {
    switch(key) {
      case "address": {
        this.address = value
        break;
      }
      case "notes": {
        this.notes = value
        break;
      }
    }
  }

  confirm() {
    console.log('confirm with address: ' + this.address + ", notes: " + this.notes)
    if (this.address.length == 0) {
      this.msg = 'address cannot be empty'
      return
    }
    this.orderService.addOrder(this.products, this.address, (info) => {
      this.basketService.orderMade()
      this.router.navigateByUrl('/dashboard');
    })
  }

}
