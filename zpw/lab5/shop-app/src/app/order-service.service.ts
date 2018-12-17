import { Injectable } from '@angular/core';
import { AuthServiceService } from './auth-service.service';
import { BasketServiceService } from './basket-service.service';
import { Router } from '@angular/router';
import { Order } from './objects/orders';
import { DbserviceService } from './dbservice.service';

@Injectable({
  providedIn: 'root'
})
export class OrderServiceService {
  public orders: Order[] = []

  constructor(
    private authService: AuthServiceService,
    private basketService: BasketServiceService,
    private router: Router,
    private dbservice: DbserviceService) {
    this.getOrders(()=>{
      console.log('orders:')
      console.log(this.orders)
    })
  }

  addOrder(products, address, callback) {
    this.dbservice.addOrder(products, address, callback)
  }


  getOrders(callback=null) {
    this.orders = this.dbservice.getOrders(callback)
    return this.orders
  }

  getProductsOfOrder(id) {
    console.log('getProductsOfOrder')
    for (let i in this.orders) {
      let o = this.orders[i]
      if (o.id == id) {
        // save to database 
        //this.db.object('/order/' + o.key).update(o)
        return o.products
      }
    }
  }

  finalizeOrder(id, callback=null) {
    console.log('finalze order')
    for (let i in this.orders) {
      let o = this.orders[i]
      if (o.id == id) {
        o.status = 'done'
        console.log('save to db')
        console.log(o)
        // save to database 
        this.dbservice.finalizeOrder(o, callback)
      }
    }
  }

  isOrderFinalized(id) {
    for (let i in this.orders) {
      let o = this.orders[i]
      if (o.id == id) {
        return (o.status == 'done')
      }
    }
    return false
  }

}
