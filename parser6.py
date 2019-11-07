def extract_image():
    import cv2
    from pdf2image import convert_from_path
    pages = convert_from_path('testresume.pdf', 500)
    for page in pages:
        page.save('out.jpg', 'JPEG')
    image = cv2.imread('out.jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    #print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        #print("[INFO] Object found. Saving locally.")
        cv2.imwrite('detected_face.jpg', roi_color)


   
    #cv2.imshow('face',roi_color)
    return roi_color
extract_image()
