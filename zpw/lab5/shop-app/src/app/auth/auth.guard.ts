import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router'; 
import { AuthServiceService } from '../auth-service.service'; 
import { map } from 'rxjs/operators'; 

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor( 
    private authService: AuthServiceService, 
    private router: Router, 
  ) {}

  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> { 
    return this.authService.authState$.pipe(map(state => {
      if (state !== null) {
        return true;
      }
      this.router.navigate(['/login']);
      return false;
    })); 
  }
}
