import { Component, OnInit } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { Order } from '../objects/orders';
import { OrderServiceService } from '../order-service.service';

@Component({
  selector: 'app-orders-management-component',
  templateUrl: './orders-management-component.component.html',
  styleUrls: ['./orders-management-component.component.scss']
})
export class OrdersManagementComponentComponent implements OnInit {
  public data: AngularFireList<any[]>

  constructor(private db: AngularFireDatabase, public orderService: OrderServiceService) { }

  ngOnInit() {
  }

  finalizeOrder(orderId) {
    this.orderService.finalizeOrder(orderId)
  }

  isFinalized(orderId) {
    return this.orderService.isOrderFinalized(orderId)
  }

}
