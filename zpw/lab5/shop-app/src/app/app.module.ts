import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsComponent } from './products/products.component';
import { SingleProductComponent } from './single-product/single-product.component';
import { NewProductComponent } from './new-product/new-product.component';
import { BasketComponent } from './basket/basket.component';
//import { Angular2FontawesomeModule } from 'angular2-fontawesome/angular2-fontawesome';
import { CheckoutComponent } from './checkout/checkout.component'
import { AngularFireAuthModule } from 'angularfire2/auth';
import { AngularFireModule } from 'angularfire2';
import { environment } from '../environments/environment'
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { LoginComponentComponent } from './login-component/login-component.component';
import { DashboardComponentComponent } from './dashboard-component/dashboard-component.component';
import { RegisterComponentComponent } from './register-component/register-component.component';
import { AdminComponentComponent } from './admin-component/admin-component.component';
import { AdminPanelComponentComponent } from './admin-panel-component/admin-panel-component.component';
import { OrdersManagementComponentComponent } from './orders-management-component/orders-management-component.component';
import { ProductsManagementComponentComponent } from './products-management-component/products-management-component.component';
import { DummyManagementComponentComponent } from './dummy-management-component/dummy-management-component.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductsComponent,
    SingleProductComponent,
    NewProductComponent,
    BasketComponent,
    CheckoutComponent,
    LoginComponentComponent,
    DashboardComponentComponent,
    RegisterComponentComponent,
    AdminComponentComponent,
    AdminPanelComponentComponent,
    OrdersManagementComponentComponent,
    ProductsManagementComponentComponent,
    DummyManagementComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    //Angular2FontawesomeModule,
    AngularFireModule.initializeApp(environment.firebaseConfig),
    AngularFireAuthModule,
    AngularFireDatabaseModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
