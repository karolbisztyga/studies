import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-panel-component',
  templateUrl: './admin-panel-component.component.html',
  styleUrls: ['./admin-panel-component.component.scss']
})
export class AdminPanelComponentComponent implements OnInit {

  public username = ''

  constructor(
    private authService:AuthServiceService,
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
