import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServoMotorComponent } from './servo-motor.component';

describe('ServoMotorComponent', () => {
  let component: ServoMotorComponent;
  let fixture: ComponentFixture<ServoMotorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ServoMotorComponent]
    });
    fixture = TestBed.createComponent(ServoMotorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
