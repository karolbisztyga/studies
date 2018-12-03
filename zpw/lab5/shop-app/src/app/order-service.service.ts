import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { AuthServiceService } from './auth-service.service';
import { BasketServiceService } from './basket-service.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class OrderServiceService {
  public data: AngularFireList<any[]>

  constructor(
    private db: AngularFireDatabase,
    private authService: AuthServiceService,
    private basketService: BasketServiceService,
    private router: Router) {
    this.data = this.db.list('/order')
  }

  addOrder(products, address, callback) {
    this.data.push([{
      user: this.authService.getUser().email,
      products: products,
      addres: address}]).then(callback)
  }
}
