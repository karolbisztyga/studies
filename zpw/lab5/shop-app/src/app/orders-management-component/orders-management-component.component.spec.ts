import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OrdersManagementComponentComponent } from './orders-management-component.component';

describe('OrdersManagementComponentComponent', () => {
  let component: OrdersManagementComponentComponent;
  let fixture: ComponentFixture<OrdersManagementComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OrdersManagementComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OrdersManagementComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
