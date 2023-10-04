import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WeightSensorComponent } from './weight-sensor.component';

describe('WeightSensorComponent', () => {
  let component: WeightSensorComponent;
  let fixture: ComponentFixture<WeightSensorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WeightSensorComponent]
    });
    fixture = TestBed.createComponent(WeightSensorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
