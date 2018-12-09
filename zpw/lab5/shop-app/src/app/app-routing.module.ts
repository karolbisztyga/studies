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
import { AdminComponentComponent } from './admin-component/admin-component.component';
import { AdminPanelComponentComponent } from './admin-panel-component/admin-panel-component.component';
import { ProductsManagementComponentComponent } from './products-management-component/products-management-component.component';
import { OrdersManagementComponentComponent } from './orders-management-component/orders-management-component.component';
import { DummyManagementComponentComponent } from './dummy-management-component/dummy-management-component.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard/products', pathMatch: 'full' },
  {
    path: 'admin',
    component: AdminComponentComponent,
    children: [
      { path: '', redirectTo: 'login', pathMatch: 'full' },
      { path: 'login', component: LoginComponentComponent },
      {
        path: 'panel',
        component: AdminPanelComponentComponent,
        canActivate: [AuthGuard],
        children: [
          { path: '', redirectTo: 'dummy', pathMatch: 'full' },
          { path: 'dummy', component: DummyManagementComponentComponent },
          { path: 'products', component: ProductsManagementComponentComponent },
          { path: 'orders', component: OrdersManagementComponentComponent },
        ]
      },
    ]
  },
  {
    path: 'dashboard',
    component: DashboardComponentComponent,
    children: [
      { path: '', redirectTo: 'products', pathMatch: 'full' },
      { path: 'products', component: ProductsComponent },
      { path: 'basket', component: BasketComponent },
      { path: 'checkout', component: CheckoutComponent },
    ]
  },
  { path: '**', redirectTo: '/dashboard/products', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
