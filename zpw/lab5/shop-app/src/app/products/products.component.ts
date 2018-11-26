import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { ProductServiceService } from '../product-service.service'
import { ProductCategory } from '../objects/product_category';
import { BasketServiceService } from '../basket-service.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
  providers: [ProductServiceService]
})
export class ProductsComponent implements OnInit {

  public products: Product[]
  public categories: ProductCategory[]
  public basketTotalPrice: number

  constructor(
    private productService:ProductServiceService,
    private basketService:BasketServiceService) {
    this.categories = [
      ProductCategory.FRUIT,
      ProductCategory.MEAL,
      ProductCategory.SWEETS,
      ProductCategory.VEGETABLE,
    ]
  }

  ngOnInit() {
    this.products = this.productService.getProducts()
    this.basketTotalPrice = this.basketService.totalPrice
  }

  /*deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    this.productService.deleteProduct(id)
  }*/

  addEvent(productId: number) {
    console.log('parent adds product')
    console.log(productId)
    this.basketService.addProduct(productId)
    this.basketTotalPrice = this.basketService.getTotalPrice()
  }

}
