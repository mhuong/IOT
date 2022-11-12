int cambien = A0; //Cảm biến nối chân số 5 Arduino
int giatri;

int den = 8; //Khai báo chân đèn nối với chân số 8 trên Arduino
int loa =10;
void setup() 
{
  Serial.begin(9600);

  pinMode(den, OUTPUT); 
   pinMode(loa, OUTPUT);
  digitalWrite(den, LOW); //Mặc định đèn tắt
  digitalWrite(loa, LOW);
  pinMode(cambien, INPUT); //Cảm biến nhận tín hiệu

}

void loop() 
{
  giatri = analogRead(cambien); //Đọc giá trị analog của cảm biến và gán vào biến giatri

  if (giatri > 200) //Nếu giá trị cảm biến gas lớn hơn 600
 {
    digitalWrite(den, HIGH); //Đèn sáng
     digitalWrite(loa, HIGH); 
  }
  else //Ngược lại
  {
    digitalWrite(den, LOW); //Đèn tắt
    digitalWrite(loa, LOW);
  }
  
  Serial.print("Giá trị cảm biến: ");
  Serial.println(giatri);
  delay(200);
}