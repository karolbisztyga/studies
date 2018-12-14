import { Component, OnInit } from '@angular/core'
import { Product } from '../objects/product'
import { ProductServiceService } from '../product-service.service'
import { BasketServiceService } from '../basket-service.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {

  public products: Product[]
  public showProducts: Product[]
  public categoriesLoaded = false
  public categories = []
  public basketTotalPrice: number
  public username = ''
  public basketMsg = ''
  public pagination = {
    productsPerSite: 3,
    site: 1,
    numSites: 0
  }

  constructor(
    private productService:ProductServiceService,
    private basketService:BasketServiceService) {
  }

  ngOnInit() {
    if (this.basketService.msg == 'order made') {
      this.basketService.msg = ''
      window.location.reload()
      return
    }
    let that = this
    this.products = this.productService.getProducts(function() {
      that.updateSort()
      that.upadtePagination()
    })
    this.basketTotalPrice = this.basketService.totalPrice
    this.basketMsg = this.basketService.msg
  }

  upadtePagination() {
    let from = (this.pagination.site - 1) * this.pagination.productsPerSite
    let to = from + this.pagination.productsPerSite
    this.pagination.numSites = Math.ceil(this.products.length / this.pagination.productsPerSite)
    this.showProducts = this.products.slice(from, to)
    console.log('pagination ' + from + ' ' + to + ' ' + this.pagination.numSites)
    console.log(this.showProducts)
  }

  incPage() {
    this.pagination.site = Math.min(this.pagination.site + 1, this.pagination.numSites)
    this.upadtePagination()
  }

  decPage() {
    this.pagination.site = Math.max(this.pagination.site - 1, 1)
    this.upadtePagination()
  }

  public currSort = {
    by: 'name',
    method: 'asc'
  }
  changeSort(key, value) {
    switch(key) {
      case 'by': {
        this.currSort.by = value
        break;
      }
      case 'method': {
        this.currSort.method = value
        break;
      }
    }
    // update
    this.updateSort()
  }

  updateSort() {
    this.products.sort((p1,p2) => {
      switch (this.currSort.by) {
        case 'name': {
          switch (this.currSort.method) {
            case 'asc': {
              return (p1.name <= p2.name) ? -1 : 1
              break
            }
            case 'desc': {
              return (p1.name > p2.name) ? -1 : 1
              break
            }
          }
          break
        }
        case 'price': {
          switch (this.currSort.method) {
            case 'asc': {
              return (p1.price_for_one <= p2.price_for_one) ? -1 : 1
              break
            }
            case 'desc': {
              return (p1.price_for_one > p2.price_for_one) ? -1 : 1
              break
            }
          }
          break
        }
      }
    })
    console.log('here')
    this.upadtePagination()
  }

  addEvent(productId: number) {
    this.basketService.addProduct(this.products, productId)
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
    this.pagination.site = 1
    console.log('update cat filters')
    this.products = []
    let allFiltersDisabled = true
    for (let i in this.categories) {
      if (this.categories[i].filter) {
        allFiltersDisabled = false
        break
      }
    }
    console.log('all filters disabled: ' + allFiltersDisabled)
    if (allFiltersDisabled) {
      for (let i in this.productService.products) {
        this.products.push(this.productService.products[i])
      }
    }
    else {
      for (let p in this.productService.products) {
        var prod = this.productService.products[p]
        for (let c in this.categories) {
          if (!this.categories[c].filter) {
            continue
          }
          let catname = this.categories[c].name
          for (let pc in prod.categories) {
            if (prod.categories.includes(catname)) {
              if (!this.products.includes(prod)) {
                this.products.push(prod)
              }
            }
          }
        }
      }
    }
    console.log('update categories')
    console.log(this.products)
    this.upadtePagination()
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
