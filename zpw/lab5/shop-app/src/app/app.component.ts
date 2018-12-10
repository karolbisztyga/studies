import { Component } from '@angular/core';
import { BasketServiceService } from './basket-service.service';
import { ProductServiceService } from './product-service.service';
import { OrderServiceService } from './order-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [BasketServiceService, ProductServiceService, OrderServiceService]
})
export class AppComponent {
  title = 'shop-app';
}
