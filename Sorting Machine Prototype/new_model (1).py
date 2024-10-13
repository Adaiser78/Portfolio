from keras.models import load_model  # TensorFlow is required for Keras to work.
print("imported keras")
    
import cv2  # Install opencv-python
print("imported cv2")
    
import numpy as np # Tensorflow uses numpy.
print("imported numpy")
   
import time # To introduce time delays.
print("imported time")

import serial # Required for the communication between the rock 4 and arduino. 
print("imported serial")

from serial.tools.list_ports import comports
   
print("imported modules successfully")

# Intialize time.
start_time = time.time()
elapsed_time = 0

changed = True
 

def InitializeSerial():

    # printing the port information
    for portItem in comports():
        print(portItem)

    # adjust the proper port, in my case it is /dev/ttyACM0
    arduinoSerial = serial.Serial(port='/dev/ttyACM0',
                                  baudrate=115200,
                                  timeout=.5)

    # check if the port is opened
    arduinoSerial.is_open

    # close the port
    arduinoSerial.close()

    # open the port
    arduinoSerial.open()

    return arduinoSerial



# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer.

camera = cv2.VideoCapture(0)

print("initialized model and camera successfully")


while True:
    
    
    print("capture loop restart")

    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    
    confidence = int(str(np.round(confidence_score * 100))[:-2])
    
    # IMPORTANT:
    # BELOW THESE LINES IS COMMUNICATION CODE. THIS IS NOT KERAS CODE. 
    
    class_classification = class_name[2:][0:7]
      
    if class_classification == "Class 1":
        signal = "00"
        changed = True
    elif class_classification == "Class 2":
        signal = "10"
    elif class_classification == "Class 3":
        signal = "01"
    else:
        signal = "11"

    signal
    print(f"Digit: {signal}")   

    arduinoSerial = InitializeSerial()

    
    
    # write the message 
    if (signal == "10" or signal == "01") and (confidence > 90) and (elapsed_time > 1.0) and changed:
        arduinoSerial.write(bytes(signal, 'utf-8'))
        start_time = time.time()
        changed = False
        
        
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    
    
    
    # IMPORTANT:
    # COMMUNICATION CODE HAS ENDED.

    # Listen to the keyboard for presses. 27 is the ASCII for the esc key on your keyboard.
    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

arduinoSerial.close()
camera.release()
cv2.destroyAllWindows()



