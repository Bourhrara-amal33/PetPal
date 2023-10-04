import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SensorListComponent } from './components/sensorList/sensorList.component';

const routes: Routes = [
  {path : 'sensordata', component : SensorListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
