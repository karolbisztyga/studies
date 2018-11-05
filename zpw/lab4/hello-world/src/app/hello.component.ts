import { Component } from '@angular/core';
import { tabliczka, tabliczka2 } from "./zad5";

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


  tab1:String[] = tabliczka(["Ala", "ma", "kota"], [1, 2, 3, 4]);
  tab2:String[] = tabliczka2(["Ala", "ma", "kota"], [1, 2, 3, 4]);

}