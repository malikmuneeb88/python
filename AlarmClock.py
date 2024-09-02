import datetime
import time
import simpleaudio as sa

def set_alarm(alarm_time):

    while True:
        current_time = datetime.datetime.now().strftime("%D-%M-%Y  %H:%M:%S")
        print("Current Date and time is ", current_time)

        if current_time == alarm_time:
            print("Its Time to wake up!!")

            wave_obj = sa.waveObject.from_wave_file('alarm_sound.wav')
            play_obj = wave_obj.play()
            play_obj.wait_done()

            time.sleep(1)
            break

date = input("Set the alarm date in (MM-DD-YY format:)\n")
time = input("Set the alarm time in (HH:MM format:)\n")

alarm_time = f"{date} {time}"

set_alarm(alarm_time)