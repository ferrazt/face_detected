import cv2
import numpy as np
from keras.models import load_model

# carregar modelo treinado
model = load_model('keras_model.h5', compile=False)

# carregar rótulos
#with open('labels.txt', 'r') as f:
    #labels = [line.strip() for line in f.readlines()]

# iniciar captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # capturar frame
    ret, frame = cap.read()

    # detectar rosto
    face_cascade = cv2.CascadeClassifier('frontal_facedetected.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # desenhar caixa delimitadora ao redor do rosto
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face = frame[y:y+h, x:x+w]
        
        # redimensionar imagem para dimensões do modelo
        face = cv2.resize(face, (224, 224))
        face = np.expand_dims(face, axis=0)

        # realizar predição
        #prediction = model.predict(face)[0]

        # determinar rótulo com base na saída do modelo
        #label = labels[np.argmax(prediction)]

        # exibir rótulo no frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "face", (x,y-10), font, 0.9, (255,0,0), 2, cv2.LINE_AA)

    # exibir frame
    cv2.imshow('frame',frame)

    # sair ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# liberar recursos
cap.release()
cv2.destroyAllWindows()
