void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
  while (!Serial) {}
}

String buffer = "";

void loop() {
  // serial read section
  while (Serial.available())  // this will be skipped if no data present, leading to
                              // the code sitting in the delay function below
  {
    delay(30);
    int b = Serial.available();
    for (int i = 0; i < b; ++i) {
      char c = Serial.read();
      buffer += String(c);
    }
    if (buffer.equals("bmk:009:getStatus\r\n")) {
      Serial.print("bmk=009 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:009:gPr\r\n")) {
      Serial.print("bmk=009 pr0=300 pr1=400 pr2=000 er=00000000 bmkC=007 prC0=003 prC1=000 erC=00000000 cs=016\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:010:getStatus\r\n")) {
      Serial.print("bmk=010 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:011:getStatus\r\n")) {
      Serial.print("bmk=011 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:012:getStatus\r\n")) {
      Serial.print("bmk=012 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:013:getStatus\r\n")) {
      Serial.print("bmk=013 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:014:getStatus\r\n")) {
      Serial.print("bmk=014 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:015:getStatus\r\n")) {
      Serial.print("bmk=015 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:016:getStatus\r\n")) {
      Serial.print("bmk=016 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:017:getStatus\r\n")) {
      Serial.print("bmk=017 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:018:getStatus\r\n")) {
      Serial.print("bmk=018 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:019:getStatus\r\n")) {
      Serial.print("bmk=019 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:020:getStatus\r\n")) {
      Serial.print("bmk=020 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    if (buffer.equals("bmk:021:getStatus\r\n")) {
      Serial.print("bmk=021 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064 P10=125 P15=219 P20=316 P25=401 P30=489 P35=581 Err=00000000 uPit=23 temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n");
      buffer = "";
    }
    buffer = "";
  }
}
