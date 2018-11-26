import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { SingleProductComponent } from './single-product/single-product.component';
import { BasketComponent } from './basket/basket.component';
import { CheckoutComponent } from './checkout/checkout.component';

const routes: Routes = [
  { path: 'products', component: ProductsComponent },
  { path: '', redirectTo: '/products', pathMatch: 'full' },
  { path: 'product/:id', component: SingleProductComponent },
  { path: 'basket', component: BasketComponent },
  { path: 'checkout', component: CheckoutComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
