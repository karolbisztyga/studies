import { Component } from '@angular/core';

@Component({
  selector: 'hello-app',
  templateUrl: './hello.component.html',
  styleUrls: ['./app.component.css']
})
export class HelloComponent {

  imie = "jan";
  nazwisko = 'kovalsky';
  updateName(newname) {
    this.imie = newname;
  }
  a = 2+3;
  url = window.location.href;

}