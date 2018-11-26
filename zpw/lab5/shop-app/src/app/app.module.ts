import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsComponent } from './products/products.component';
import { SingleProductComponent } from './single-product/single-product.component';
import { NewProductComponent } from './new-product/new-product.component';
import { BasketComponent } from './basket/basket.component';
import { Angular2FontawesomeModule } from 'angular2-fontawesome/angular2-fontawesome';
import { CheckoutComponent } from './checkout/checkout.component'

@NgModule({
  declarations: [
    AppComponent,
    ProductsComponent,
    SingleProductComponent,
    NewProductComponent,
    BasketComponent,
    CheckoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    Angular2FontawesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
