/* =====================================================================
 * EXPERIMENT PART A: IMU bias & noise characterization
 * Board: Arduino UNO R4 WiFi   
 * Sensor: 7Semi BNO055
 *
 * GOAL: Keep the sensor perfectly still for ~60 s and compute, for all
 * six channels (ax ay az gx gy gz):
 *      1. Bias  = mean − expected value
 *      2. Noise = sqrt( mean of squares − square of mean )
 *
 * TODO: Complete 1 to 4 in order. Do not modify setup() or loop().
 * ===================================================================== */
#include <Wire.h>
#include <7Semi_BNO055.h>

BNO055_7Semi imu;

const int N = 5000;// ~60 s of samples
const char*  name[6]     = {"ax", "ay", "az", "gx", "gy", "gz"};
const double expected[6] = {0, 0, 9.81, 0, 0, 0};      // True values (NO MOVEMENT OF THE SENSOR)

double sum[6] = {0, 0, 0, 0, 0, 0}, 
double sumSq[6] = {0, 0, 0, 0, 0, 0};
int n = 0;

// DO NOT EDIT THIS FUNCTION
void setup() {
  Serial.begin(115200);
  while (!Serial);
  
  if (!imu.begin()) 
  { 
    Serial.println("BNO055 not found"); 
    while (1); 
  }
  
  imu.setMode(Mode::ACCGYRO); // Raw mode
  delay(1000); // 1 second delay
  Serial.println("Measuring for ~60 s - DO NOT TOUCH/MOVE THE SENSOR");
}

// DO NOT TOUCH THIS FUNCTION
void loop() {
  int16_t axr, ayr, azr, gxr, gyr, gzr;
  double  s[6];

  // TODO 1
  if (!readSensors(axr, ayr, azr, gxr, gyr, gzr)) {
    Serial.println("LINK LOST");
    delay(10);
    return;
  }

  // TODO 2
  convertToUnits(axr, ayr, azr, gxr, gyr, gzr, s);

  // TODO 3
  accumulate(s);

  if (n == N) {
    // TODO 4 
    printResults();
    while (1);
  }
  delay(10);
}

/* ---------------------------------------------------------------------
 * TODO 1 — Complete the following function: readSensors
 * Ask the BNO055 for its raw accelerometer and gyroscope counts - Call 
 * imu.readAccel(axr, ayr, azr) and imu.readGyro(gxr, gyr, gzr).
 * --------------------------------------------------------------------- */
bool readSensors(int16_t &axr, int16_t &ayr, int16_t &azr,
                 int16_t &gxr, int16_t &gyr, int16_t &gzr) {
  // Your code here

  return false;   // <-- replace "false" with your result
}

/* ---------------------------------------------------------------------
 * TODO 2 — Complete the following function: convertToUnits (units)
 * The sensor provides raw integer values. 
 * STEP 1: Convert:
 *   s[0..2] = axr, ayr, azr divided by 100.0  → m/s²  (100 counts per m/s²)
 *   s[3..5] = gxr, gyr, gzr divided by 16.0   → °/s   (16 counts per °/s)
 * STEP 2: Pack into s[]
 * --------------------------------------------------------------------- */
void convertToUnits(int16_t axr, int16_t ayr, int16_t azr,
                    int16_t gxr, int16_t gyr, int16_t gzr, double s[6]) {
  // Your code here

}

/* ---------------------------------------------------------------------
 * TODO 3 — Complete the following function: accumulate
 * The mean needs only the running TOTAL; 
 * The standard deviation needs only the running TOTAL OF SQUARES.
 * LOGIC: 
 * For each channel i = 0 to 5:
 *   a) add s[i] into sum[i]
 *   b) add s[i]*s[i] into sumSq[i]
 * Then count this sample: increase n by 1.
 * --------------------------------------------------------------------- */
void accumulate(double s[6]) {
  // Your code here
}

/* ---------------------------------------------------------------------
 * TODO 4 — Complete the following function: printResults
 * For each channel i = 0 to 5, compute and print:
 *   mean  = sum[i] / n
 *   sigma = sqrt( sumSq[i]/n − mean*mean )
 *   bias  = mean − expected[i]
 * Print one line per channel:  name, bias, noise (use 4 decimals).
 * --------------------------------------------------------------------- */
void printResults() {
  Serial.println("--- RESULTS for Table 1 ---");
  // Your code here

}



