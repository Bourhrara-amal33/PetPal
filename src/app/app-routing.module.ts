import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SensorListComponent } from './components/sensorList/sensorList.component';
import { HomeComponent } from './home/home.component';
import { ServoMotorComponent } from './components/servo-motor/servo-motor.component';
import { CameraDataComponent } from './components/camera-data/camera-data.component';
import { WeightSensorComponent } from './components/weight-sensor/weight-sensor.component';

const routes: Routes = [
  {path : 'sensordata', component : SensorListComponent},
  {path : '', component : HomeComponent },
  { path: 'servomotor', component: ServoMotorComponent },
  { path: 'cameradata', component: CameraDataComponent },
  { path: 'weightdata', component: WeightSensorComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
