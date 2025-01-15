import cv2
import cvzone
from ultralytics import YOLO
import math
import threading
import ollama
from gtts import gTTS
import os
import queue

model = YOLO("./runs/detect/train2/weights/last.pt")
print(f"Available model names: {model.names}")
q = queue.Queue(maxsize=6)
threads = {}

def reader():
    while True:
        filename = q.get()
        print(f"Working on {filename}")
        os.system(f"afplay {filename}")
        q.task_done()

threading.Thread(target=reader, daemon=True).start()


def text_to_speech(text, roi_id):
    res = gTTS(text=text, lang='en')
    filename = f"./speech/{roi_id}_output.mp3"
    res.save(filename)
    q.put(filename)

def get_details(image_file, class_name, roi_id):
    print("processing " + image_file + " of class " + class_name)

    res = ollama.chat(
	    model="llava:7b",
	    messages=[
		    {
			    'role': 'user',
			    'content': 'Describe a ' + class_name + " recognized inside the rectangle. Make it very short and concise. Very important: Do not mention any rectangle nor image - it's only technical. Instead use words like \"I can see...\".",
			    'images': [image_file],
		    }
	    ]
    )
    print(image_file + " of class " + class_name + ": " + res['message']['content'])
    text_to_speech(res['message']['content'], roi_id)
    threads.pop(roi_id)

if __name__ == "__main__":
    recognized_objects = {}
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        results = model.track(frame, persist=True, verbose=False)
        frame = results[0].plot()
        for box in results[0].boxes:
            if box.id == None:
                continue
            id = box.id.item()
            name = model.names[int(box.cls[0])]
            if id not in recognized_objects:
                recognized_objects[id] = "./images/roi" + str(id) + ".jpg"
                cv2.imwrite(recognized_objects[id], frame)
                t = threading.Thread(target=get_details, args=(recognized_objects[id], name, id))
                t.start()
                threads[id] = t
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break        

for thread in threads.values():
    thread.join(0)

