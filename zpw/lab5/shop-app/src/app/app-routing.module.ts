import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { SingleProductComponent } from './single-product/single-product.component';
import { BasketComponent } from './basket/basket.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { LoginComponentComponent } from './login-component/login-component.component';
import { AuthGuard } from './auth/auth.guard';
import { DashboardComponentComponent } from './dashboard-component/dashboard-component.component';
import { RegisterComponentComponent } from './register-component/register-component.component';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponentComponent },
  { path: 'register', component: RegisterComponentComponent },
  {
    path: 'dashboard',
    component: DashboardComponentComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', redirectTo: 'products', pathMatch: 'full' },
      { path: 'products', component: ProductsComponent },
      { path: 'product/:id', component: SingleProductComponent },
      { path: 'basket', component: BasketComponent },
      { path: 'checkout', component: CheckoutComponent },
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
