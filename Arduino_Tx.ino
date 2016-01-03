#define TxPin 4
int _transmitPin = 4;
int b = 142;

int WriteDelay_uS = 8;

byte mask = 1; // BYTE is important here!! otherwise don't get 8bit mask


int baudrate = 400;
int delay_uS = round(1000000/baudrate);

int counter = 0;
int counter2 = 0;
void setup()
{
  Serial.begin(9600);
  pinMode(TxPin,OUTPUT);
  digitalWrite(TxPin,LOW);

  delay(2000);
  Serial.println(delay_uS);
  Serial.println("go");
}



void loop(){

  b=counter;

  Serial.println(b,BIN);
  digitalWrite(_transmitPin, HIGH);
  delayMicroseconds(delay_uS);//-WriteDelay_uS);
  digitalWrite(TxPin,LOW);
  delayMicroseconds(delay_uS);
  for (mask = 00000001; mask>0; mask <<= 1) {	//bitshifts left 8 times: 00000001->0000010 etc
    if (b & mask){ // choose bit
      digitalWrite(_transmitPin,HIGH); // send 1 if bit at current position is a 1, hence bitwise AND: 0b01 & 0b01 = 1 but 0b10 & 0b01 = 0
    }
    else{
      digitalWrite(_transmitPin,LOW); // send 0
    }
    delayMicroseconds(delay_uS);//-WriteDelay_uS);
  }

  digitalWrite(TxPin,LOW);
  delayMicroseconds(delay_uS);
  digitalWrite(_transmitPin, HIGH);
  delayMicroseconds(2*delay_uS);//-WriteDelay_uS);

  

  //Serial.println("sent");
//  delay(3000);

  counter2++;

  if (counter2%10==0){
    delay(2000);
  }

  if(counter<256){
    counter++;
  }
  else{
    counter = 1;
  }
} 


