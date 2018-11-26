import { Component } from '@angular/core';
import { BasketServiceService } from './basket-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [BasketServiceService]
})
export class AppComponent {
  title = 'shop-app';
}
