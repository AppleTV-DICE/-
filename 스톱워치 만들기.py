import tkinter as tk
import time

# tkinter 창 생성
root = tk.Tk()
root.title("스톱워치")

# 시간 표시를 위한 라벨
time_label = tk.Label(root, text="00:00:00.000", font=("Helvetica", 36))
time_label.pack(padx=20, pady=20)

# 시간 변수 초기화
start_time = None
laps = []

# 시간 업데이트 함수
def update_time():
    if start_time:
        passed_time = time.time() - start_time
        minutes, seconds = divmod(passed_time, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((passed_time - int(passed_time)) * 1000)
        time_string = "{:02d}:{:02d}:{:02d}.{:03d}".format(int(hours), int(minutes), int(seconds), milliseconds)
        time_label.config(text=time_string)
        time_label.after(1, update_time)

# 스톱워치 제어 함수
def start():
    global start_time
    if not start_time:
        start_time = time.time()
        update_time()

def stop():
    global start_time
    start_time = None

def reset():
    global start_time, laps
    start_time = None
    time_label.config(text="00:00:00.000")
    laps = []
    laps_listbox.delete(0, tk.END)

def lap():
    if start_time:
        passed_time = time.time() - start_time
        minutes, seconds = divmod(passed_time, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((passed_time - int(passed_time)) * 1000)
        lap_time = "{:02d}:{:02d}:{:02d}.{:03d}".format(int(hours), int(minutes), int(seconds), milliseconds)
        laps.append(lap_time)
        laps_listbox.insert(tk.END, f"Lap {len(laps)}: {lap_time}")

# 버튼 생성
start_button = tk.Button(root, text="시작", command=start)
start_button.pack(padx=20, pady=5)

stop_button = tk.Button(root, text="중지", command=stop)
stop_button.pack(padx=20, pady=5)

reset_button = tk.Button(root, text="리셋", command=reset)
reset_button.pack(padx=20, pady=5)

lap_button = tk.Button(root, text="랩", command=lap)
lap_button.pack(padx=20, pady=5)

# 랩 타임 표시를 위한 리스트 박스
laps_listbox = tk.Listbox(root, height=5)
laps_listbox.pack(padx=20, pady=20)

root.mainloop()
