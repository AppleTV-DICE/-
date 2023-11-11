import tkinter as tk
from tkinter import messagebox
import random


def generate_random_number():
    """
    0부터 9까지 서로 다른 세 숫자로 이루어진 랜덤한 숫자를 생성합니다.
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:3]


def check_guess(target, guess):
    """
    추측한 숫자와 정답을 비교하여 S, B, O를 반환합니다.
    """
    strikes = sum(x == y for x, y in zip(target, guess))
    balls = sum(x in guess for x in target) - strikes
    outs = 3 - (strikes + balls)
    return strikes, balls, outs


def submit_guess():
    global attempts, attempts_label

    user_guess = entry.get()

    try:
        user_guess = list(map(int, user_guess))
        if len(user_guess) != 3 or any(x < 0 or x > 9 for x in user_guess) or len(set(user_guess)) != 3:
            raise ValueError
    except ValueError:
        #messagebox.showerror("입력 오류", "올바른 입력이 아닙니다. 0부터 9까지 서로 다른 세 숫자를 입력하세요.")
        messagebox.showerror("야", "재밌다")
        return

    strikes, balls, outs = check_guess(target_number, user_guess)
    result_label.config(text=f"S:{strikes}, B:{balls}, O:{outs}")

    attempts += 1
    attempts_label.config(text=f"시도 횟수: {attempts}")

    if strikes == 3:
        messagebox.showinfo("게임 종료", "축하합니다! 정답을 맞췄습니다.")
        window.quit()
    elif attempts == 10:
        messagebox.showinfo("게임 종료", f"10회의 기회를 모두 사용했습니다. 정답은 {target_number}")
        window.quit()
    else:
        guesses_listbox.insert(tk.END,
                               f"{attempts}. {''.join(map(str, user_guess))} - S:{strikes}, B:{balls}, O:{outs}")
        entry.delete(0, tk.END)  # 입력 값 초기화


# 윈도우 설정
window = tk.Tk()
window.title("야구 게임")

# 랜덤한 숫자 생성
target_number = generate_random_number()
attempts = 0

# 라벨 및 엔트리 위젯 추가
instruction_label = tk.Label(window, text="0부터 9까지 서로 다른 세 숫자를 입력하세요:")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="제출", command=submit_guess)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

attempts_label = tk.Label(window, text="시도 횟수: 0")
attempts_label.pack()

guesses_listbox = tk.Listbox(window, height=5, width=30)
guesses_listbox.pack()

window.mainloop()