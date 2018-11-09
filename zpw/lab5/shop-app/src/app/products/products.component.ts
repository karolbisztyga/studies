import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { products } from '../objects/fake_products'

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {

  public products: Product[] = products
  constructor() {

  }

  ngOnInit() {

  }

  deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    for (let p of products) {
      if (id == p.id) {
        console.log('deleting ' + p.name)
        const index:number = products.indexOf(p)
        if (index > -1) {
          products.splice(index, 1)
        }
      }
    }
  }

}
