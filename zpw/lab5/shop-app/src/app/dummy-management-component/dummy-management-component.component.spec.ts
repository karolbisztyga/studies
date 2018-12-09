import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DummyManagementComponentComponent } from './dummy-management-component.component';

describe('DummyManagementComponentComponent', () => {
  let component: DummyManagementComponentComponent;
  let fixture: ComponentFixture<DummyManagementComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DummyManagementComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DummyManagementComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
