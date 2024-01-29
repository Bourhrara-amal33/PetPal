import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CameraDataComponent } from './camera-data.component';

describe('CameraDataComponent', () => {
  let component: CameraDataComponent;
  let fixture: ComponentFixture<CameraDataComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CameraDataComponent]
    });
    fixture = TestBed.createComponent(CameraDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
