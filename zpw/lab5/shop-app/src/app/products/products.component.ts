import { Component, OnInit } from '@angular/core';
import { Product } from '../objects/product'

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {

  public products: Product[] = [
    new Product(1, 'apple', 2542, 2.5, 'fresh tasty apples are good for you', 'https://i5.walmartimages.ca/images/Large/428/5_r/6000195494285_R.jpg'),
    new Product(2, 'banana', 125, 3.7, 'only yellow bananas are good', 'https://images-na.ssl-images-amazon.com/images/I/71gI-IUNUkL._SY355_.jpg'),
    new Product(3, 'sandwich', 30, 15.79, 'sandwich with ham, cheese and ketchup', 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/2017/05/main/egg-in-nest-blt-sandwiches-1707p38.jpg?itok=-2zHWRHS'),
    new Product(4, 'onion', 125, 3.7, 'it is very healthy though', 'https://image.shutterstock.com/image-photo/red-gold-onions-isolated-on-260nw-569575726.jpg'),
    new Product(5, 'chocolate', 88, 10.32, 'anything with chocolate is good, right', 'https://www.history.com/.image/t_share/MTU3ODc4NjAyOTgyNjk2Njcx/hungry-sweet-chocolate-istock_000027210034large-2.jpg')
  ]
  constructor() {

  }

  ngOnInit() {

  }

  deleteEvent(id: number) {
    console.log('parent deletes product ' + id)
    for (let p of this.products) {
      if (id == p.id) {
        console.log('deleting ' + p.name)
        // todo
      }
    }
  }

}
