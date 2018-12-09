import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register-component',
  templateUrl: './register-component.component.html',
  styleUrls: ['./register-component.component.scss']
})
export class RegisterComponentComponent implements OnInit {

  public email = ''
  public password = ''
  public msg = ''

  constructor(
    private authService: AuthServiceService,
    private router: Router) { }

  ngOnInit() {
  }

  update(item: string, data: string) {
    switch(item) {
      case 'email': {
        this.email = data
        break
      }
      case 'password': {
        this.password = data
        break
      }
    }
  }

  register() {
    console.log('registering: ' + this.email + '/' + this.password)
    if (this.password.length == 0 || this.email.length == 0) {
      this.msg = 'register failed'
      return
    }
    // check email
    if (!this.validateEmail(this.email)) {
      this.msg = 'register failed'
      return
    }
    let result = this.authService.register({email: this.email, password: this.password}, (userInfo) => {
      this.msg = ''
      this.router.navigateByUrl('/dashboard/login');
    }, (error) => {
      this.msg = 'register failed'
      console.log(error)
    })
  }

  validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }

}
