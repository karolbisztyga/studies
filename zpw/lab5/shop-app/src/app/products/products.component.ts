import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { ProductServiceService } from '../product-service.service'

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
  providers: [ProductServiceService]
})
export class ProductsComponent implements OnInit {

  public products: Product[] 
  constructor(private productService:ProductServiceService) {
    this.products = productService.getProducts()
  }

  ngOnInit() {

  }

  deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    this.productService.deleteProduct(id)
  }

}
