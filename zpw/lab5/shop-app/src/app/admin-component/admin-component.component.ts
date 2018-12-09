import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-component',
  templateUrl: './admin-component.component.html',
  styleUrls: ['./admin-component.component.scss']
})
export class AdminComponentComponent implements OnInit {

  public email = ''
  public password = ''
  public msg = ''

  constructor(
    private authService: AuthServiceService,
    private router: Router) { }

  ngOnInit() {
  }

  updateData(key, val) {
    switch(key) {
      case 'email': {
        this.email = val
        break;
      }
      case 'password': {
        this.password = val
        break;
      }
    }
  }

  login() {
    console.log('logging in as ' + this.email)
    let result = this.authService.login({email: this.email, password: this.password}, (userInfo) => {
      this.msg = ''
      console.log('loged in as ' + this.email)
      this.router.navigateByUrl('/admin/panel');
    }, (error) => {
      this.msg = 'login failed'
      console.log(error)
    })
  }

}
