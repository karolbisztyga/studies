import { Injectable } from '@angular/core';
import { FirebaseHandler } from './database_handlers/firebaseHandler';
import { MongoHandler } from './database_handlers/mongoHandler';
import { DatabaseHandler } from './database_handlers/databaseHandler';
import { AngularFireDatabase } from 'angularfire2/database';
import { Product } from './objects/product';
import { Http } from '@angular/http';

@Injectable({
  providedIn: 'root'
})
export class DbserviceService {

  private firebase: FirebaseHandler
  private mongo: MongoHandler

  public databases = [
    'firebase',
    'mongo',
  ]

  public databaseHandler: DatabaseHandler = null

  constructor(
      private db: AngularFireDatabase,
      private http: Http) {
    this.firebase = new FirebaseHandler()
    this.mongo = new MongoHandler()
    this.getDatabase()
  }

  getDatabase() {
    var ls = null
    if (localStorage.getItem('db') !== null) {
      ls = localStorage.getItem('db')
    }
    console.log('local storage: ' + ls)
    console.log(ls)
    if (!ls) {
      ls = 'firebase'
    }
    if (this.databases.includes(ls)) {
      // firebase
      if (ls == this.databases[0]) {
        this.databaseHandler = this.firebase
      }
      // mongo
      else if (ls == this.databases[1]) {
        this.databaseHandler = this.mongo
      }
    }
    return this.databaseHandler
  }

  getTool() {
    this.getDatabase()
    if (this.databaseHandler == this.firebase) {
      return this.db
    }
    if (this.databaseHandler == this.mongo) {
      return this.http
    }
  }

  changeDatabase(db) {
    if (this.databaseHandler.name == db) {
      return false
    }
    if (!this.databases.includes(db)) {
      return false
    }
    console.log('change db from '  + this.databaseHandler + ' to ' + db)
    this.databaseHandler = db
    localStorage.setItem('db', db)
    return true
  }

  private getCookie(name) {
    let ca: Array<string> = document.cookie.split(';');
    let caLen: number = ca.length;
    let cookieName = `${name}=`;
    let c: string;

    for (let i: number = 0; i < caLen; i += 1) {
        c = ca[i].replace(/^\s+/g, '');
        if (c.indexOf(cookieName) == 0) {
            return c.substring(cookieName.length, c.length);
        }
    }
    return '';
  }

  private setCookie(name, value, expireDays, path = '') {
      let d:Date = new Date();
      d.setTime(d.getTime() + expireDays * 24 * 60 * 60 * 1000);
      let expires:string = `expires=${d.toUTCString()}`;
      let cpath:string = path ? `; path=${path}` : '';
      document.cookie = `${name}=${value}; ${expires}${cpath}`;
  }

  /*
    DATABASE METHODS
  */

  getProducts(callback=null) {
    let tool = this.getTool()
    return this.databaseHandler.getProducts(tool, callback)
  }

  getCategories(callback=null) {
    let tool = this.getTool()
    return this.databaseHandler.getCategories(tool, callback)
  }
  
  addProduct(product: Product, callback=null) {
    let tool = this.getTool()
    return this.databaseHandler.addProduct(tool, product, callback)
  }
  
  saveProduct(product: Product, callback=null) {
    let tool = this.getTool()
    return this.databaseHandler.saveProduct(tool, product, callback)
  }
  
  getOrders(callback) {
    let tool = this.getTool()
    return this.databaseHandler.getOrders(tool, callback)
  }
  
  finalizeOrder(order, callback=null) {
    let tool = this.getTool()
    return this.databaseHandler.finalizeOrder(tool, order, callback)
  }
  
  addOrder(products, address, callback) {
    let tool = this.getTool()
    return this.databaseHandler.addOrder(tool, products, address, callback)
  }

}
