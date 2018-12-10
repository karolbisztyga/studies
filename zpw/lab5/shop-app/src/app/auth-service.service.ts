import { Injectable } from '@angular/core';
import { AngularFireAuth } from 'angularfire2/auth';
import { User } from 'firebase';
import { Observable } from 'rxjs/index';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';

export interface Credentials {
  email: string
  password: string
}

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {
  public data: AngularFireList<any[]>
  private admins = []

  constructor(private fireAuth:AngularFireAuth,
      private db: AngularFireDatabase) {
        this.data = this.db.list('/admin_roles')
        this.data.valueChanges().subscribe(res => {
          for (let i in res) {
            this.admins.push(res[i])
          }
        })
      }

  getUser(): User | null {
    return this.fireAuth.auth.currentUser
  }

  login({email, password}: Credentials, callback, errCallback) {
    let res = this.fireAuth.auth.signInWithEmailAndPassword(email, password)
        .then(callback)
        .catch(errCallback)
    return res
  }

  register({email, password}: Credentials, callback, errCallback) {
    return this.fireAuth.auth.createUserWithEmailAndPassword(email,password)
        .then(callback)
        .catch(errCallback);
  }

  logout() {
    return this.fireAuth.auth.signOut();
  }

  isAdmin(email) {
    return (this.admins.includes(email))
  }

  readonly authState$: Observable<User | null> = this.fireAuth.authState;
}

