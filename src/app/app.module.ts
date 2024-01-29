import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { initializeApp,provideFirebaseApp } from '@angular/fire/app';
import { environment } from '../environments/environment';
import { provideAuth,getAuth } from '@angular/fire/auth';
import { provideDatabase,getDatabase } from '@angular/fire/database';
import { SensorListComponent } from './components/sensorList/sensorList.component';
import { FIREBASE_OPTIONS } from '@angular/fire/compat';
import { WeightSensorComponent } from './components/weight-sensor/weight-sensor.component';
import { HomeComponent } from './home/home.component';
import { ServoMotorComponent } from './components/servo-motor/servo-motor.component';
import { CameraDataComponent } from './components/camera-data/camera-data.component';

@NgModule({
  declarations: [
    AppComponent,
    SensorListComponent,
    WeightSensorComponent,
    HomeComponent,
    ServoMotorComponent,
    CameraDataComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    provideFirebaseApp(() => initializeApp(environment.firebase)),
    provideAuth(() => getAuth()),
    provideDatabase(() => getDatabase()),
    provideFirebaseApp(() => initializeApp({"projectId":"petpal-petfeeder","appId":"1:52379806500:web:f8ed53a199b66a579f21b1","databaseURL":"https://petpal-petfeeder-default-rtdb.europe-west1.firebasedatabase.app","storageBucket":"petpal-petfeeder.appspot.com","apiKey":"AIzaSyCWxiH9ZmnWOjX3_cr_cGmMNkaTUsUnlBY","authDomain":"petpal-petfeeder.firebaseapp.com","messagingSenderId":"52379806500"}))
  ],
  providers: [{ provide: FIREBASE_OPTIONS, useValue: environment.firebase }],
  bootstrap: [AppComponent]
})
export class AppModule { }