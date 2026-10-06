# Meredith Aguirre NC = 0013
import cv2

# Cargar la imagen
imagen = cv2.imread("tigre.jpg")

# Comprobar que la imagen fue cargada
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes mediante Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar resultados
cv2.imshow("Imagen original del tigre 0013", imagen)
cv2.imshow("Imagen en escala de grises del tigre 0013", gris)
cv2.imshow("Bordes Canny", bordes)

# Guardar resultado
cv2.imwrite("../resultados/ejemplo1_canny.jpg", bordes)

print("Detección de bordes completada.")
print("Resultado guardado en resultados/ejemplo1_canny.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Meredith Aguirre NC 0013")