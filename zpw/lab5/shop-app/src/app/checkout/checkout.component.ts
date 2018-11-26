import { Component, OnInit } from '@angular/core';
import { BasketServiceService } from '../basket-service.service';
import { Product } from '../objects/product';
import { Router } from '@angular/router';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss']
})
export class CheckoutComponent implements OnInit {
  public products: Product[]
  public price: number
  public address: string
  public notes: string

  constructor(private basketService: BasketServiceService,
    private router: Router) {
  }

  ngOnInit() {
    this.products = this.basketService.basketProducts
    // if there are no products, redirect to /products
    if (this.products.length == 0) {
      this.router.navigateByUrl('products')
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
  }

}
