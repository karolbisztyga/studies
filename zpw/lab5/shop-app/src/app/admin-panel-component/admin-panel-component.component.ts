import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';
import { ProductServiceService } from '../product-service.service';
import { OrderServiceService } from '../order-service.service';

@Component({
  selector: 'app-admin-panel-component',
  templateUrl: './admin-panel-component.component.html',
  styleUrls: ['./admin-panel-component.component.scss']
})
export class AdminPanelComponentComponent implements OnInit {

  public username = ''

  constructor(
    public authService:AuthServiceService,
    private router: Router) { }

  ngOnInit() {
    this.username = this.authService.getUser().email
  }
  
  logout() {
    console.log('logging out ' + this.username)
    this.authService.logout()
    this.router.navigateByUrl('/admin');
  }

  

}
