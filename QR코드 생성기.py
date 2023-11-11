
'''import tkinter as tk
import qrcode
from PIL import Image, ImageTk

# 데이터
data = "https://www.naver.com"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# tkinter 창 생성
root = tk.Tk()
root.title("QR 코드 생성기")

# 이미지를 tkinter로 표시
tk_img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=tk_img)
label.pack(padx=20, pady=20)

root.mainloop()
'''
import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# tkinter 창 생성
root = tk.Tk()
root.title("QR 코드 생성기")

# 입력 받기 위한 함수
def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    tk_img = ImageTk.PhotoImage(img)
    label.config(image=tk_img)
    label.image = tk_img
    global qr_image
    qr_image = img

# 저장 함수
def save_qr_code():
    if 'qr_image' in globals():
        file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG 파일", "*.png")])
        if file_name:
            qr_image.save(file_name)

# 입력 필드 생성
entry = tk.Entry(root)
entry.pack(padx=20, pady=10)

# 버튼 생성
generate_button = tk.Button(root, text="생성", command=generate_qr_code)
generate_button.pack(padx=20, pady=10)

save_button = tk.Button(root, text="저장", command=save_qr_code)
save_button.pack(padx=20, pady=10)

# 라벨 생성
label = tk.Label(root)
label.pack(padx=20, pady=20)

root.mainloop()