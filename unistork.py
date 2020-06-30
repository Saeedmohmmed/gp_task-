import tkinter as tk
import os
import pyautogui
import win32gui


name = None
def screen(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1-70))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im



def final():
    im = screen("tk")
    if im:
        im.save(r'pic.png')
        import imageToText
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=400, height=400, bg = "black", cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button_print = tk.Button(self, text = "grab text", command = final)
        self.button_print.pack(side="top", fill="both", expand=True)
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)

    def clear_all(self):
        self.canvas.delete("all")

    def print_points(self):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.canvas.create_line(self.points_recorded, fill = "white")
        self.points_recorded[:] = []

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y, 
                                self.x, self.y,fill="yellow")
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)     
        self.points_recorded.append(self.x)        
        self.previous_x = self.x
        self.previous_y = self.y



if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()


