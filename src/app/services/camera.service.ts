import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { CameraData } from '../shared/camera-data'; 

@Injectable({
  providedIn: 'root',
})
export class CameraService {
  private basePath = '/camera_data'; // Ajoutez le chemin correct pour votre base de données

  constructor(private db: AngularFireDatabase) {}

  addCameraData(data: CameraData) {
    // Générer une nouvelle clé pour chaque entrée
    const key = this.db.createPushId();

    // Définir la clé et ajouter les données à la base de données
    return this.db.object(`${this.basePath}/${key}`).set({ key, ...data });
  }

  getCameraDataList() {
    return this.db.list<CameraData>(this.basePath).valueChanges();
  }
}
