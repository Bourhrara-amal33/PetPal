import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SensorListComponent } from './components/sensorList/sensorList.component';
import { HomeComponent } from './home/home.component';
import { ServoMotorComponent } from './components/servo-motor/servo-motor.component';


const routes: Routes = [
  {path : 'sensordata', component : SensorListComponent},
  {path : '', component : HomeComponent },
  { path: 'servomotor', component: ServoMotorComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
