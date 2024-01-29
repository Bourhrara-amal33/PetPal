import { TestBed } from '@angular/core/testing';

import { WeightSensorService } from './weight-sensor.service';

describe('WeightSensorService', () => {
  let service: WeightSensorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WeightSensorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
