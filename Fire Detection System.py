import time
import RPi.GPIO as GPIO

# GPIO pin configuration
FLAME_SENSOR_PIN = 17
BUZZER_PIN = 27
RED_LED_PIN = 22

# Most flame sensor modules output LOW when fire is detected
FIRE_DETECTED_STATE = GPIO.LOW

GPIO.setmode(GPIO.BCM)

GPIO.setup(
    FLAME_SENSOR_PIN,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)

GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_LED_PIN, GPIO.OUT, initial=GPIO.LOW)

print("Fire detection system started.")
print("Monitoring for flames...")

try:
    while True:
        flame_status = GPIO.input(FLAME_SENSOR_PIN)

        if flame_status == FIRE_DETECTED_STATE:
            print("WARNING: Flame detected!")

            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            GPIO.output(RED_LED_PIN, GPIO.HIGH)

        else:
            print("No flame detected.")

            GPIO.output(BUZZER_PIN, GPIO.LOW)
            GPIO.output(RED_LED_PIN, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nStopping fire detection system...")

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.cleanup()
