import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { AuthServiceService } from './auth-service.service';
import { BasketServiceService } from './basket-service.service';
import { Router } from '@angular/router';
import { Order } from './objects/orders';

@Injectable({
  providedIn: 'root'
})
export class OrderServiceService {
  public data: AngularFireList<any[]>
  public orders: Order[] = []

  constructor(
    private db: AngularFireDatabase,
    private authService: AuthServiceService,
    private basketService: BasketServiceService,
    private router: Router) {
    this.getOrders(()=>{
      console.log('orders:')
      console.log(this.orders)
    })
  }

  addOrder(products, address, callback) {
    let totalPrice = 0
    for (let i in products) {
      let p = products[i]
      totalPrice += p.total_price
    }
    let date = new Date().toDateString()
    this.data.push([{
      products: products,
      address: address,
      totalPrice: totalPrice,
      date: date,
      status: 'waiting'}]).then(callback)
  }


  getOrders(callback=null) {
    if (this.orders.length > 0) {
      return this.orders
    }
    this.data = this.db.list('/')
    //console.log('data from DATABASE')
    //console.log(this.data)
    var id = 1
    this.data.valueChanges().subscribe(res => {
      let orders = res[res.length-2]
      console.log('result:')
      console.log(orders)
      for (let i in orders) {
        let item = orders[i][0]
        //console.log('item')
        //console.log(item)
        let order: Order = new Order()
        order.address = item['address']
        order.products = item['products']
        order.totalPrice = item['totalPrice']
        order.id = id++
        order.key = i
        this.orders.push(order)
      }
      if (callback) {
        callback()
      }
    })
    return this.orders
  }

  getproductsoforder(id) {
    for (let i in this.orders) {
      let o = this.orders[i]
      if (o.id == id) {
        // save to database 
        //this.db.object('/order/' + o.key).update(o)
        return o.products
      }
    }
  }

  finalizeOrder(id) {
    for (let i in this.orders) {
      let o = this.orders[i]
      if (o.id == id) {
        o.status = 'done'
        console.log('save to db')
        // save to database 
        this.db.object('/order/' + o.key).update(o)
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
