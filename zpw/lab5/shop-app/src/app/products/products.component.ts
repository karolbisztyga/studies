import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { ProductServiceService } from '../product-service.service'
import { BasketServiceService } from '../basket-service.service';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
  providers: [ProductServiceService]
})
export class ProductsComponent implements OnInit {

  public products: Product[]
  public categoriesLoaded = false
  public categories = []
  public basketTotalPrice: number
  public username = ''
  public basketMsg = ''

  constructor(
    private productService:ProductServiceService,
    private basketService:BasketServiceService) {
  }

  ngOnInit() {
    this.products = this.productService.getProducts()
    this.basketTotalPrice = this.basketService.totalPrice
    this.basketMsg = this.basketService.msg
    console.log('basket msg: ' + this.basketMsg)
    if (this.basketMsg.length > 0) {
      this.basketService.msg = ''
    }
  }

  /*deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    this.productService.deleteProduct(id)
  }*/

  addEvent(productId: number) {
    this.basketService.addProduct(productId)
    this.basketTotalPrice = this.basketService.getTotalPrice()
  }

  cat_select(event, cat) {
    if (this.categoriesLoaded === false) {
      this.categories = []
      for (let i in this.productService.categories) {
        this.categories.push({ name: this.productService.categories[i], filter: false})
      }
      this.categoriesLoaded = true
    }
    for (let i in this.categories) {
      if (this.categories[i].name == cat) {
        this.categories[i].filter = !this.categories[i].filter
      }
    }
    this.updateCatFilters()
  }

  showFilter(cat) {
    cat = this.productService.categories[cat]
    for (let i in this.categories) {
      if (this.categories[i].name == cat) {
        return this.categories[i].filter
      }
    }
  }

  updateCatFilters() {
    console.log('update cat filters')
    this.products = []
    let allFiltersDisabled = true
    for (let i in this.categories) {
      if (this.categories[i].filter) {
        allFiltersDisabled = false
        break
      }
    }
    if (allFiltersDisabled) {
      for (let i in this.productService.products) {
        this.products.push(this.productService.products[i])
      }
      return
    }
    for (let p in this.productService.products) {
      var prod = this.productService.products[p]
      for (let c in this.categories) {
        if (!this.categories[c].filter) {
          continue
        }
        let catname = this.categories[c].name
        for (let pc in prod.categories) {
          if (prod.categories.includes(catname)) {
            this.products.push(prod)
          }
        }
      }
    }
  }
/*
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
