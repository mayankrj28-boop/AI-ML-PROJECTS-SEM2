import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class FaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Face Detection System")
        self.root.geometry("900x700")
        self.root.configure(bg="#121212")

        self.cap = None
        self.running = False

        # Title
        self.title = tk.Label(root, text="AI Face Detection",
                              font=("Helvetica", 24, "bold"),
                              fg="white", bg="#121212")
        self.title.pack(pady=20)

        # Video Display
        self.video_label = tk.Label(root, bg="black")
        self.video_label.pack()

        # Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#121212")
        self.btn_frame.pack(pady=20)

        self.start_btn = tk.Button(self.btn_frame, text="Start Camera",
                                  command=self.start_camera,
                                  bg="#00c853", fg="white",
                                  font=("Helvetica", 12), width=15)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(self.btn_frame, text="Stop Camera",
                                 command=self.stop_camera,
                                 bg="#d50000", fg="white",
                                 font=("Helvetica", 12), width=15)
        self.stop_btn.grid(row=0, column=1, padx=10)

        # Status Label
        self.status = tk.Label(root, text="Status: Camera Off",
                               font=("Helvetica", 12),
                               fg="white", bg="#121212")
        self.status.pack()

    def start_camera(self):
        if not self.running:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.status.config(text="Status: Camera ON")
            self.update_frame()

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.video_label.config(image="")
        self.status.config(text="Status: Camera OFF")

    def update_frame(self):
        if self.running:
            ret, frame = self.cap.read()

            if ret:
                frame = cv2.flip(frame, 1)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                # Draw face boxes
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, "Face", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

                # Face count
                cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

                # Convert to Tkinter format
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)

                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

            self.root.after(10, self.update_frame)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceApp(root)
    root.mainloop()
