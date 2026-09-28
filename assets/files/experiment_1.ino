/*
 * 25PC2RA202 - S&A Lab | Experiment 1: Odometry and Kinematics
 * Quadrature encoder, 1x decoding (count rising edges of Phase A)
 */

const int PIN_A = 2;           // Phase A (Green wire)  -> D2 (interrupt)
const int PIN_B = 3;           // Phase B (White wire)  -> D3
const float N   = 360.0;       // counts per revolution (1x decoding)

volatile long pulseCount = 0;  // updated inside the ISR

void setup() {
  Serial.begin(115200);
  pinMode(PIN_A, INPUT_PULLUP);
  pinMode(PIN_B, INPUT_PULLUP);

  // TODO 1: Attach an interrupt that calls encoderISR() on every
  //         RISING edge of Phase A.
  attachInterrupt(digitalPinToInterrupt(PIN_A), ____, ____);
}

void loop() {
  // TODO 3: Calculate the measured angle (in degrees) from pulseCount and N.
  float angle = ____;

  Serial.print("Count: ");
  Serial.print(pulseCount);
  Serial.print("\tAngle: ");
  Serial.println(angle);
  delay(200);
}

void encoderISR() {
  // TODO 2: Read Phase B. If it is LOW, the shaft is rotating
  //         clockwise -> increment pulseCount; otherwise decrement it.
}
