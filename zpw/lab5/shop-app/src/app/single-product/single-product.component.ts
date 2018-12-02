import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../objects/product'

@Component({
  selector: 'app-single-product',
  templateUrl: './single-product.component.html',
  styleUrls: ['./single-product.component.scss']
})
export class SingleProductComponent implements OnInit {

  @Input() product:Product;
  @Output('add') addEvent = new EventEmitter<number>()

  detailed = false

  constructor() {
  }

  ngOnInit() {
    //console.log(this.product.img_url)
  }
  
  add_current(event) {
    this.addEvent.emit(this.product.id)
  }

  change_detailed() {
    this.detailed = !this.detailed
  }

  isDetailed() {
    return this.detailed
  }
}