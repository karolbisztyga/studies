import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard-component',
  templateUrl: './dashboard-component.component.html',
  styleUrls: ['./dashboard-component.component.scss']
})
export class DashboardComponentComponent implements OnInit {

  public username = ''

  constructor(
    private authService:AuthServiceService,
    private router: Router) { }

  ngOnInit() {
    this.username = this.authService.getUser().email
  }

  logout() {
    this.authService.logout()
    this.router.navigateByUrl('/login');
  }

}
