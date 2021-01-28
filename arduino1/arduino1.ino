
int bot = 7;
int botmenos =6;
int botmais = 5;
int fase;
int estadobot;
int estadomais;
int estadomenos;
int antimais;
int antimenos;
int antibot;
int tempo;
int f;
int t;
void setup() {
  Serial.begin(9600);


  // put your setup code here, to run once:
  pinMode(botmais,INPUT);
  pinMode(botmenos,INPUT);
  pinMode(bot,INPUT);
  pinMode(12,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(13,OUTPUT);
  digitalWrite(12,LOW);
  fase = 0;
  tempo = 0;

  Serial.print(" fase=");
  Serial.print(fase,"  ");
  Serial.print('\n');
  Serial.print(" tempo=");
  Serial.print(tempo,"  " );
  
}

void loop() {
  
  
  if (f != fase){
    
  Serial.print(" fase=");
  Serial.print(fase);
  Serial.print('\n');
  delay(100);
  }
  if (t != tempo){
  
  Serial.print(" tempo=");
  Serial.print(tempo);
  delay(100);
  }
  f = fase;
  t = tempo;
    estadobot = digitalRead(bot);
    estadomais = digitalRead(botmais);
    estadomenos = digitalRead(botmenos);
  if(Serial.available()){
  
    }
  

  if ((estadobot == HIGH)&&(antibot == LOW)){
    
    if(fase < 1){
      
      fase = fase + 1;
      }else{
      fase = 0;
      }
    
    }
    if ((estadomais == HIGH)&&(antimais == LOW)){
      tempo = tempo + 5;
      digitalWrite(10,HIGH);
      delay(500);
      digitalWrite(10,LOW);
      Serial.print(tempo);
      
      
    }else{
      digitalWrite(9,HIGH);
      delay(500);
      digitalWrite(9,LOW);
     
      }

  
  

  // put your main code here, to run repeatedly:
  while (fase == 1){
   if (f != fase){
    
  Serial.print(" fase=");
  Serial.print(fase,"  ");
  Serial.print('\n');
  }
  if (t != tempo){
  
  Serial.print(" tempo=");
  Serial.print(tempo,"  " );
  Serial.print('\n');
  }
  f = fase;
  t = tempo;
      delay(500);
      digitalWrite(13,HIGH);
    Serial.print(tempo);
    estadobot = digitalRead(bot);
    if ((estadobot == HIGH)&&(antibot == LOW)){
    
    if(fase < 1){
      
      fase = fase + 1;
      }else{
      fase = 0;
      }
   
    }
    antibot = estadobot;
    if(tempo != 0){
      Serial.print(tempo);
      tempo = tempo - 1;
      delay(500);
    }
    
    if((tempo == 0)&&(fase == 1)){
      digitalWrite(12,HIGH);
    }else{
      digitalWrite(12,LOW);
    }
  
    }
    antimenos = estadomenos;
    antimais = estadomais;
    antibot = estadobot;
  }
