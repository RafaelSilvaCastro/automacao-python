# pip install opencv-python

# Abrindo a camera e fazendo o reconecimento facil

import cv2 

# pegando a camera do computador
camera = cv2.VideoCapture(0)

# carregar o arquivo treinado para detectar faces
cascadeFace = cv2.CascadeClassifier("reconhecimento_facial/haarcascade_frontalface_default.xml")

# loop para percorrer frame a frame, ou imagem por imagem
while True:
    sucesso, frame = camera.read()
    
    # converter a imagem para tons de cinza
    imagemTonsDeCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # utilizar arquivo de detecção
    faces = cascadeFace.detectMultiScale(imagemTonsDeCinza, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

    # desenhar um retangulo na imagem
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    # exibi a imagem detectada
    cv2.imshow("imagem video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("s"): # se a teclado do teclado for S ele sai do loop
        break

camera.release()
cv2.destroyAllWindows()
        

#############################################
# Apenas mostrar a camera 

# import cv2 

# # criando uma variavel para capiturar imagens(frames)
# # video = cv2.VideoCapture("python_senai/05/aula1105-webcam/midias/video.mp4")

# # pegando a camera do computador
# camera = cv2.VideoCapture(0)

# # loop para percorrer frame a frame, ou imagem por imagem
# while True:
#     sucesso, frame = camera.read()
#     cv2.imshow("imagem video", frame)
    
#     if cv2.waitKey(1) & 0xFF == ord("s"): # se a teclado do teclado for S ele sai do loop
#         break

# camera.release()
# cv2.destroyAllWindows()
    