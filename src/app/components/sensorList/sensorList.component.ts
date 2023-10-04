import { Component, OnInit } from '@angular/core';
import { AngularFireList, AngularFireDatabase } from '@angular/fire/compat/database';
import { map } from 'rxjs/operators';

interface SensorData {
  $key?: string;
  delay?: number;
  date?: string;
  time?: string;
  device?: string;
}

@Component({
  selector: 'app-sensorList',
  templateUrl: './sensorList.component.html',
  styleUrls: ['./sensorList.component.css']
})
export class SensorListComponent implements OnInit {

  private SensorzRef: AngularFireList<SensorData>;
  public sensorData?: SensorData[];
  currentSensorData?: SensorData;
  currentIndex = -1;
  device = '';

  constructor(db: AngularFireDatabase) { 
    this.SensorzRef = db.list<SensorData>('/ultrasound_distance');
  }

  ngOnInit(): void {
    this.SensorzRef
      .snapshotChanges()
      .pipe(
        map(changes => changes.map(c => ({...c.payload.val() } as SensorData)))
      )
      .subscribe(data => {
        this.sensorData = data;
      });
  }
}
