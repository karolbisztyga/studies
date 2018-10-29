import { TestBed, async } from '@angular/core/testing';
import { HelloComponent } from './hello.component';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        HelloComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(HelloComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'hello-world'`, () => {
    const fixture = TestBed.createComponent(HelloComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.title).toEqual('hello-world');
  });

  it('should render title in a h1 tag', () => {
    const fixture = TestBed.createComponent(HelloComponent);
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('h1').textContent).toContain('Welcome to hello-world!');
  });
});
