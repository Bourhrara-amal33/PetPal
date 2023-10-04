import { Component, OnInit } from '@angular/core';
import { DbService } from 'src/app/services/db.service'; // Adjust the import path
import { SensorData } from 'src/app/shared/model'; // Adjust the import path

@Component({
  selector: 'app-sensorList',
  templateUrl: './sensorList.component.html',
  styleUrls: ['./sensorList.component.css']
})
export class SensorListComponent implements OnInit {
  sensorDataList: SensorData[] = [];
  currentSensorData?: SensorData;
  currentIndex = -1;
  device = '';

  constructor(private dbService: DbService) { }

  ngOnInit(): void {
    this.retrieveSensorData();
  }

  // Retrieve the list of sensor data records
  retrieveSensorData(): void {
    this.dbService.getSensorDataList().subscribe(data => {
      this.sensorDataList = data;
    });
  }





}
