import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Product } from '../objects/product'

@Component({
  selector: 'app-new-product',
  templateUrl: './new-product.component.html',
  styleUrls: ['./new-product.component.scss']
})
export class NewProductComponent implements OnInit {

  //public product:Product = new Product()
  @Output('add') addEvent = new EventEmitter<Product>()

  constructor() { }

  ngOnInit() {
  }
  
  updateInfo(key, value) {
    /*switch(key) {
      case 'name': {
        this.product.name = value
        break
      }
      case 'quantity': {
        this.product.quantity = value
        break
      }
      case 'price': {
        this.product.price_for_one = value
        break
      }
      case 'description': {
        this.product.description = value
        break
      }
      case 'image': {
        this.product.img_url = value
        break
      }
    }*/
  }

  add(event) {
    //this.addEvent.emit(this.product)
  }

}
