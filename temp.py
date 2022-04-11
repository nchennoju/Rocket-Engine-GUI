void printData() {

  dataline = String(batteryVoltage);    0
  dataline += ',';

  for (int i = 0; i < 10; i++) {        1,2,3,4,5,6,7,8,9,10
    dataline += String(solenoidState[i]);
    dataline += ',';
  }

  for (int i = 0; i < 10; i++) {        11,12,13,14,15,16,17,18,19,20
    dataline += String(solenoidCurrent[i]);
    dataline += ',';
  }

  dataline += String(v3RegulatorCurrent);       21
  dataline += ',';
  dataline += String(v5RegulatorCurrent);       22
  dataline += ',';
  dataline += String(v12RegulatorCurrent);      23
  dataline += ',';

  for (int i = 1; i <= 10; i++) {               24,25,26,27,28,29,30,31,32,33
    dataline += String(pressureSensor[i]);
    dataline += ',';
  }

  for (int i = 1; i <= 4; i++) {                34,35,36,37
    dataline += String(analogInput[i]);
    dataline += ',';
  }

  for (int i = 0; i < 10; i++) {                38,39,40,41,42,43,44,45,46,47
    dataline += String(thermocouple[i]);
    dataline += ',';
  }

  dataline += String(analogRead(A20));          48
  dataline += ',';


  dataline += String(millis());                 49

  //log to SD card
  char filename[fileName.length() + 1];
  fileName.toCharArray(filename, fileName.length()+1);
  logfile = SD.open(filename, FILE_WRITE);
  if(logfile) {
    logfile.println(dataline);
    dataline += ",1,";
    digitalWrite(led, LOW);
  }else{
    dataline += ",0,";
    digitalWrite(led, HIGH);
  }

  dataline += String(heartbeat);

  logfile.close();
  Serial.println(dataline);
  Serial5.println(dataline); //added

  // reset heartbeat
  if(millis() - heartbeatStart > HEARTBEAT_SPAN) {
    heartbeat = false;
  }

}
