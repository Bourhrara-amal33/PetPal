// servo-motor.component.ts

import { Component } from '@angular/core';
import { ServoMotorService } from '../../services/servo-motor.service';

@Component({
  selector: 'app-servo-motor',
  templateUrl: './servo-motor.component.html',
  styleUrls: ['./servo-motor.component.css']
})
export class ServoMotorComponent {
  constructor(private servoMotorService: ServoMotorService) {}

  onLeftButtonClick(): void {
    this.addServoMotorData(true, false); // Left button clicked
  }

  onRightButtonClick(): void {
    this.addServoMotorData(false, true); // Right button clicked
  }

  private addServoMotorData(left: boolean, right: boolean): void {
    const servoMotorData = {
      date: this.getCurrentDate(),
      left: left,
      right: right,
      time: this.getCurrentTime(),
      device: 'servo-motor'
    };

    this.servoMotorService.addServoMotorData(servoMotorData)
      .then(() => console.log('Servo motor data added to Firebase'))
      .catch(error => console.error('Error adding servo motor data:', error));
  }

  private getCurrentDate(): string {
    const currentDate = new Date();
    return currentDate.toISOString().split('T')[0];
  }

  private getCurrentTime(): string {
    const currentTime = new Date();
    return currentTime.toTimeString().split(' ')[0];
  }
}
