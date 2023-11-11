import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("그림판")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.brush_size_label = ttk.Label(root, text="브러쉬 크기:")
        self.brush_size_label.pack()

        self.brush_size_slider = ttk.Scale(root, from_=1, to=20, orient="horizontal")
        self.brush_size_slider.set(5)  # 초기 브러쉬 크기 설정
        self.brush_size_slider.pack()

        self.color_button = ttk.Button(root, text="색상 선택", command=self.choose_color)
        self.color_button.pack()

        self.save_button = ttk.Button(root, text="저장", command=self.save_canvas)
        self.save_button.pack()

        self.clear_button = ttk.Button(root, text="전체 초기화", command=self.clear_canvas)
        self.clear_button.pack()

        self.clear_button = ttk.Button(root, text="안녕", command=self.clear_canvas)
        self.clear_button.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.is_drawing = False
        self.last_x = None
        self.last_y = None
        self.current_color = "black"  # 초기 색상 설정

    def start_drawing(self, event):
        self.is_drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.is_drawing:
            brush_size = self.brush_size_slider.get()
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.current_color, width=brush_size)
            self.last_x = x
            self.last_y = y

    def choose_color(self):
        color = askcolor()[1]  # 사용자에게 색상 선택 대화 상자를 열어 선택한 색상을 가져옴
        if color:
            self.current_color = color

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG 파일", "*.png"), ("모든 파일", "*.*")])
        if file_path:
            try:
                # Create a blank image with the same size as the canvas
                image = Image.new("RGB", (self.canvas.winfo_width(), self.canvas.winfo_height()), "white")
                draw = ImageDraw.Draw(image)

                # Iterate through canvas items and draw them on the image
                for item in self.canvas.find_all():
                    coords = self.canvas.coords(item)
                    color = self.canvas.itemcget(item, "fill")
                    width = round(float(self.canvas.itemcget(item, "width")))  # 부동 소수점 값을 반올림하여 정수로 변환
                    draw.line(coords, fill=color, width=width)

                # Save the image to the specified file path
                image.save(file_path)
                print(f"그림을 {file_path}로 저장했습니다.")
            except Exception as e:
                print(f"저장 중 오류 발생: {e}")

    def clear_canvas(self):
        self.canvas.delete("all")  # 캔버스에서 모든 그림 삭제

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
