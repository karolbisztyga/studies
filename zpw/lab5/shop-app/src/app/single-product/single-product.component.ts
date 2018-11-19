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

  constructor() {
  }

  ngOnInit() {
  }
  
  add_current(event) {
    this.addEvent.emit(this.product.id)
  }
}