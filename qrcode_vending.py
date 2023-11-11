import tkinter as tk
from tkinter import messagebox
from qrcode import make
from PIL import Image, ImageTk
import sqlite3
import cv2
from pyzbar.pyzbar import decode

class SushiVendingMachine:
   def __init__(self, master):
       self.master = master
       self.balance = self.update_balance_label()
       self.food_items = {'초밥': 10, '돈카츠': 15, '우동': 8, '라멘': 12, 'VIP': 100000000000000000000000000000000}
       self.selected_item = tk.StringVar()

       self.label = tk.Label(master, text="현재 잔액: ₩{}".format(self.balance))
       self.label.pack()

       for item in self.food_items.keys():
           tk.Radiobutton(master, text=item, variable=self.selected_item, value=item).pack()

       self.buy_button = tk.Button(master, text="구매", command=self.buy_item)
       self.buy_button.pack()

       self.charge_button = tk.Button(master, text="QR 코드로 충전", command=self.charge_button_click)
       self.charge_button.pack()

   def update_balance_label(self):
       conn = sqlite3.connect('vending_machine.db')
       cursor = conn.cursor()

       cursor.execute('SELECT balance FROM users WHERE id = 1')
       current_balance = cursor.fetchone()[0]

       conn.close()
       return current_balance

   def buy_item(self):
       item = self.selected_item.get()
       if item in self.food_items and self.food_items[item] <= self.balance:
           self.balance -= self.food_items[item]
           self.label.config(text="현재 잔액: ₩{}".format(self.balance))
           print(f'{item}을/를 구매했습니다!')
       else:
           print(f'잔액이 부족하거나 {item}이/가 품절되었습니다.')

   def generate_qr_code(self):
       conn = sqlite3.connect('vending_machine.db')
       cursor = conn.cursor()

       cursor.execute('SELECT balance FROM users WHERE id = 1')
       current_balance = cursor.fetchone()[0]

       # 임시로 QR 코드 생성을 위해 이미지로 잔액을 저장
       img = make(f'현재 잔액: ₩{current_balance}')
       img.save('temp_qr.png')

       conn.close()

       return 'temp_qr.png'

   def show_qr_code(self):
       qr_code_path = self.generate_qr_code()

       qr_code_window = tk.Toplevel(self.master)
       qr_code_window.title("QR 코드로 충전")

       qr_code_image = Image.open(qr_code_path)
       qr_code_photo = ImageTk.PhotoImage(qr_code_image)
       qr_code_label = tk.Label(qr_code_window, image=qr_code_photo)
       qr_code_label.image = qr_code_photo
       qr_code_label.pack()

       qr_code_window.after(5000, lambda: qr_code_window.destroy())  # 5초 후에 자동으로 창을 닫음

       return self.read_qr_code(qr_code_path)

   def read_qr_code(self, frame):
       qr_code_data = decode(frame)
       if qr_code_data:
           return float(qr_code_data[0].data)
       return None

   def charge_balance_from_qr(self, amount):
       conn = sqlite3.connect('vending_machine.db')
       cursor = conn.cursor()

       cursor.execute('SELECT balance FROM users WHERE id = 1')
       current_balance = cursor.fetchone()[0]

       new_balance = current_balance + amount
       cursor.execute('UPDATE users SET balance = ? WHERE id = 1', (new_balance,))

       conn.commit()
       conn.close()

       return new_balance

   def charge_button_click(self):
       amount = self.scan_qr_code()
       if amount is not None:
           new_balance = self.charge_balance_from_qr(amount)
           if new_balance is not None:
               self.balance = new_balance
               self.label.config(text="현재 잔액: ₩{}".format(new_balance))
               messagebox.showinfo("충전 성공", f"₩{amount}를 충전했습니다.")
           else:
               messagebox.showerror("충전 실패", "DB 오류가 발생했습니다.")
       else:
           messagebox.showerror("충전 실패", "QR 코드를 읽어올 수 없습니다.")

   def scan_qr_code(self):
       cap = cv2.VideoCapture(0)
       while True:
           ret, frame = cap.read()
           if not ret:
               break
           cv2.imshow("QR Scanner", frame)
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break

           qr_code_data = self.read_qr_code(frame)
           if qr_code_data is not None:
               cap.release()
               cv2.destroyAllWindows()
               return qr_code_data

       cap.release()
       cv2.destroyAllWindows()
       return None

if __name__ == '__main__':
   conn = sqlite3.connect('vending_machine.db')
   cursor = conn.cursor()
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           balance REAL
       )
   ''')
   cursor.execute('INSERT OR IGNORE INTO users (id, balance) VALUES (1, 10000)')
   conn.commit()
   conn.close()

   root = tk.Tk()
   app = SushiVendingMachine(root)
   root.mainloop()



import turtle

# 태양 그리기
sun = turtle.Turtle()
sun.color("yellow")
sun.shape("circle")

# 행성 그리기
planet = turtle.Turtle()
planet.color("purple")
planet.shape("circle")
planet.penup()
planet.goto(0, -140)

# 공전 경로 그리기
for _ in range(654355454364544653):
    planet.circle(140, 20)  # 반지름 50, 각도 10

turtle.done()

# 터틀 화면 생성 및 배경 색상 설정
screen = turtle.Screen()
screen.bgcolor("black")  # 배경 색상을 'lightblue'로 설정