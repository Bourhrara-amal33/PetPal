import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { SensorData } from '../shared/model';
import { AngularFireList, AngularFireObject } from '@angular/fire/compat/database';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class DbService {

  private basePath = '/ultrasound_distance'; 
  constructor(private db: AngularFireDatabase) { }


  // Get a list of sensor data records
  getSensorDataList(): Observable<SensorData[]> {
    const dataRef: AngularFireList<SensorData> = this.db.list(this.basePath);
    return dataRef.valueChanges();
  }

  // Get a specific sensor data record by key NOT USED NOW, MIGHTHELP IN FUTURE
  getSensorDataByKey(key: string): AngularFireObject<SensorData> {
    const dataRef: AngularFireObject<SensorData> = this.db.object(`${this.basePath}/${key}`);
    return dataRef;
  }


}
