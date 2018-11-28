import { Injectable } from '@angular/core';
import { AngularFireAuth } from 'angularfire2/auth';
import { User } from 'firebase';
import { Observable } from 'rxjs/index';

export interface Credentials {
  email: string
  password: string
}

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private fireAuth:AngularFireAuth) { }

  getUser(): User | null {
    return this.fireAuth.auth.currentUser
  }
  login({email, password}: Credentials) {
    return this.fireAuth.auth.signInWithEmailAndPassword(email, password);
  }

  register({email, password}: Credentials) {
    return this.fireAuth.auth.createUserWithEmailAndPassword(email,password);
  }

  logout() {
    return this.fireAuth.auth.signOut();
  }
  readonly authState$: Observable<User | null> = this.fireAuth.authState;
}

