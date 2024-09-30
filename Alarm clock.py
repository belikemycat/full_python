import time
import pygame
import datetime

def set_alarm(alarmtime):
    print(f"Alarm set for {alarmtime}")
    isActive = True
    sound_file = "roi.mp3"

    while isActive:
        current = datetime.datetime.now().strftime("%H:%M:%S")
        print(current)
        if alarm_time == alarmtime:
            print("Wake up , time to grow.")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isActive = False
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)