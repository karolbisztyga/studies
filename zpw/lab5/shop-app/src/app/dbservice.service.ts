import { Injectable } from '@angular/core';
import { FirebaseHandler } from './database_handlers/firebaseHandler';
import { MongoHandler } from './database_handlers/mongoHandler';
import { DatabaseHandler } from './database_handlers/databaseHandler';
import { AngularFireDatabase } from 'angularfire2/database';
import { Product } from './objects/product';

@Injectable({
  providedIn: 'root'
})
export class DbserviceService {

  private cookieName = 'database'
  private firebase: FirebaseHandler
  private mongo: MongoHandler

  public databases = [
    'firebase',
    'mongo',
  ]

  public databaseHandler: DatabaseHandler = null

  constructor(private db: AngularFireDatabase) {
    this.firebase = new FirebaseHandler()
    this.mongo = new MongoHandler()
    this.getDatabase()
  }

  getDatabase() {
    console.log('database get cookie: ')
    let cookie = this.getCookie(this.cookieName)
    console.log(cookie)
    if (!cookie) {
      cookie = 'firebase'
    }
    if (this.databases.includes(cookie)) {
      // firebase
      if (cookie == this.databases[0]) {
        this.databaseHandler = this.firebase
      }
      // mongo
      else if (cookie == this.databases[1]) {
        this.databaseHandler = this.mongo
      }
    }
    return this.databaseHandler
  }

  changeDatabase(db) {
    if (this.databaseHandler == db) {
      return
    }
    if (!this.databases.includes(db)) {
      return
    }
    console.log('change db from '  + this.databaseHandler + ' to ' + db)
    this.databaseHandler = db
    this.setCookie(this.cookieName, this.databaseHandler, 999)
    return this.databaseHandler
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
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.getProducts(this.db, callback)
  }

  getCategories(callback=null) {
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.getCategories(this.db, callback)
  }
  
  addProduct(product: Product) {
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.addProduct(this.db, product)
  }
  
  saveProduct(product: Product) {
    if (!this.databaseHandler) {
      this.getDatabase()
      return this.databaseHandler.saveProduct(this.db, product)
    }
    return this.databaseHandler.saveProduct(this.db, product)
  }
  
  getOrders(callback) {
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.getOrders(this.db, callback)
  }
  
  finalizeOrder(order) {
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.finalizeOrder(this.db, order)
  }
  
  addOrder(products, address, callback) {
    if (!this.databaseHandler) {
      this.getDatabase()
    }
    return this.databaseHandler.addOrder(this.db, products, address, callback)
  }

}
