// weight-sensor.service.ts
import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { Observable } from 'rxjs';
import { AngularFireList, AngularFireObject } from '@angular/fire/compat/database';
import { WeightSensor } from '../shared/weight-data'; // Assurez-vous que le chemin est correct

@Injectable({
  providedIn: 'root',
})
export class WeightSensorService {
  private basePath = '/weight_sensor_data'; // Changez le chemin selon vos besoins

  constructor(private db: AngularFireDatabase) {}

  addWeightSensorData(data: WeightSensor): Promise<void> {
    // Générer une nouvelle clé pour chaque entrée
    const key = this.db.createPushId();

    // Définir la clé et ajouter les données à la base de données
    return this.db.object(`/weightSensorData/${key}`).set({ key, ...data });
  }

  getWeightSensorDataList(): Observable<WeightSensor[]> {
    const dataRef = this.db.list<WeightSensor>(this.basePath);
    return dataRef.valueChanges();
  }

  
  // Get a specific sensor data record by key NOT USED NOW, MIGHTHELP IN FUTURE
  getSensorDataByKey(key: string): AngularFireObject<WeightSensor> {
    const dataRef: AngularFireObject<WeightSensor> = this.db.object(`${this.basePath}/${key}`);
    return dataRef;
  }

}
