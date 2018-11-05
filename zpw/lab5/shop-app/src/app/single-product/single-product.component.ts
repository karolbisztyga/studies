import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../objects/product'

@Component({
  selector: 'app-single-product',
  templateUrl: './single-product.component.html',
  styleUrls: ['./single-product.component.scss']
})
export class SingleProductComponent implements OnInit {

  @Input() product:Product;
  @Output('delete') deleteEvent = new EventEmitter<number>()

  constructor() {
  }

  ngOnInit() {
  }
  
  delete_current(event) {
    this.deleteEvent.emit(this.product.id)
  }
}