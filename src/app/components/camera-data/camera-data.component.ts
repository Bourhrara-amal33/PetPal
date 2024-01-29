
import { Component, OnInit } from '@angular/core';
import { CameraService } from '../../services/camera.service';
import { CameraData } from '../../shared/camera-data';

@Component({
  selector: 'app-camera-data',
  templateUrl: './camera-data.component.html',
  styleUrls: ['./camera-data.component.css']
})
export class CameraDataComponent implements OnInit {
  cameraDataList: CameraData[] = [];

  constructor(private cameraDataService: CameraService) { }

  ngOnInit(): void {
    this.retrieveCameraData();
  }

  // Retrieve the list of camera data records
  retrieveCameraData(): void {
    this.cameraDataService.getCameraDataList().subscribe(data => {
      console.log('Camera Data:', data); 
      this.cameraDataList = data;
    });
  }

  hasImageUrl(): boolean {
    return this.cameraDataList.some(data => !!data.imageUrl);
  }

  hasVideoUrl(): boolean {
    return this.cameraDataList.some(data => !!data.videoUrl);
  }

  hasLiveStreamUrl(): boolean {
    return this.cameraDataList.some(data => !!data.liveStreamUrl);
  }


}
