// servo-motor.service.ts

import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { ServoMotor } from '../shared/ServoMotor';

@Injectable({
  providedIn: 'root',
})
export class ServoMotorService {
  constructor(private db: AngularFireDatabase) {}

  addServoMotorData(data: ServoMotor) {
    // Generate a new key for each entry
    const key = this.db.createPushId();

    // Set the key and add the data to the database
    return this.db.object(`/servoMotorData/${key}`).set({ key, ...data });
  }

  getServoMotorDataList() {
    return this.db.list<ServoMotor>('/servoMotorData').valueChanges();
  }
}
