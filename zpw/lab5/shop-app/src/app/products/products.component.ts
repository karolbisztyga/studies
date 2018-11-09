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
  }

  ngOnInit() {
    this.products = this.productService.getProducts()
  }

  deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    this.productService.deleteProduct(id)
  }

  addEvent(product: Product) {
    console.log('parent adds product')
    console.log(product)
    this.productService.addProduct(product)
  }

}
