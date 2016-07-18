void setup() {
 Serial.begin(57600);
 Serial1.begin(57600);
}

void loop() {
  String s = "{\"temp\":25,\"hum\":30,\"ser\":\"off\",\"fan\":\"on\"}";
  int l = s.length();
  char c[l+1];
  s.toCharArray(c, l+1);
  Serial.println(c);
  Serial1.println(s);
  delay(1000);

}
