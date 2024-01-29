import { Component, OnInit } from '@angular/core';
import { WeightSensorService } from '../../services/weight-sensor.service';
import { WeightSensor } from '../../shared/weight-data'; // Assurez-vous que le chemin est correct


@Component({
  selector: 'app-weight-sensor',
  templateUrl: './weight-sensor.component.html',
  styleUrls: ['./weight-sensor.component.css']
})
export class WeightSensorComponent implements OnInit {
  weightSensorDataList: WeightSensor[] = [];

  constructor(private weightSensorService: WeightSensorService) {}

  ngOnInit(): void {
    this.retrieveWeightSensorData();
  }

  // Récupérer la liste des enregistrements de données du capteur de poids
  retrieveWeightSensorData(): void {
    this.weightSensorService
      .getWeightSensorDataList()
      .subscribe((data) => (this.weightSensorDataList = data));
  }
}
