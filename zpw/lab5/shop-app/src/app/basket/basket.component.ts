import { Component, OnInit } from '@angular/core';
import { BasketServiceService } from '../basket-service.service';
import { Product } from '../objects/product';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.scss'],
  providers: [BasketServiceService]
})
export class BasketComponent implements OnInit {
  public products: Product[]
  public price: number
  constructor(private basketService: BasketServiceService) {
  }

  ngOnInit() {
    this.products = this.basketService.basketProducts
    this.price = this.basketService.getTotalPrice()
    console.log('HEREEEEE ' + this.price)
  }

}
