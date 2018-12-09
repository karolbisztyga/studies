import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductsManagementComponentComponent } from './products-management-component.component';

describe('ProductsManagementComponentComponent', () => {
  let component: ProductsManagementComponentComponent;
  let fixture: ComponentFixture<ProductsManagementComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProductsManagementComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProductsManagementComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
