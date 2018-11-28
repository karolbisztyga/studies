import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { ProductServiceService } from '../product-service.service'
import { ProductCategory } from '../objects/product_category';
import { BasketServiceService } from '../basket-service.service';
import { Observable } from 'rxjs';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';

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

  public data: AngularFireList<any[]>

  constructor(
    private productService:ProductServiceService,
    private basketService:BasketServiceService,
    private db: AngularFireDatabase) {
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
    this.data = this.db.list('/product')
    console.log('data from DATABASE')
    this.data.valueChanges().subscribe(res => {
      console.log('+++')
      console.log(res)
    })
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

  public getdata(listPath): Observable<any[]> {
    return this.db.list(listPath).valueChanges()
  }
  /*
  adddata(value: string): void {
    this.data.push({ content: value, done: false });
  }

  updatedata(cos: any): void {
    this.db.object('/test/' + cos.$key)
    .update({/* Json * / });
  }

  deletedata(cos: any): void {
    this.db.object('/test/' + cos.$key).remove();
  }
  */
}
