# 📞 Twilio API con Flask

Este proyecto es una API en **Flask** para realizar llamadas y enviar SMS usando **Twilio**.

## 🚀 Características

- 📞 Realizar llamadas con mensajes personalizados.
- ✉️ Enviar SMS a números en formato internacional (`+1234567890`).
- 🔐 Variables de entorno para mayor seguridad.
- ✅ Probado con **Thunder Client**.

---

## 🛠️ Instalación

### 1️⃣ Clonar el repositorio

```sh
 git clone https://github.com/tu_usuario/tu_repositorio.git
 cd tu_repositorio
```

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)

```sh
python -m venv venv
# Activar en Windows:
venv\Scripts\activate
# Activar en macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```sh
pip install -r requirements.txt
```

---

## 🔐 Configuración

### 1️⃣ Crear un archivo `.env`

En la raíz del proyecto, crea un archivo `.env` con:

```ini
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

### 2️⃣ Cargar variables en el código

En `config.py` ya está configurado:

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
```

---

## ⚠️ Importante: Restricciones de Twilio (Modo Prueba)

Para usar Twilio en **modo de prueba**, debes:

1. **Crear una cuenta en Twilio** en [twilio.com](https://www.twilio.com/).
2. **Verificar un número de teléfono** desde la consola de Twilio.
3. **Solo podrás llamar y enviar SMS a números registrados en Twilio** hasta que actualices tu cuenta a producción.
4. **Cuando realizes un llamada en modo de prueba escucharas un mensaje predeterminado** presiona el boton 1 para escuchar tu mensaje.

---

## 🚀 Ejecución

Para iniciar el servidor Flask:

```sh
python main.py
```

Si todo está bien, deberías ver:

```
 * Running on http://127.0.0.1:5000/
```

---

## 🛠️ Endpoints y Pruebas

### 📞 Realizar una llamada

- **Método:** `POST`
- **URL:** `http://127.0.0.1:5000/api/calls/make`
- **Body (JSON):**

```json
{
  "to": "+1234567890",
  "message": "¡Hola! Esta es una llamada de prueba."
}
```

- **Respuesta:**

```json
{
  "success": true,
  "sid": "CA1234567890abcdef"
}
```

### ✉️ Enviar un SMS

- **Método:** `POST`
- **URL:** `http://127.0.0.1:5000/api/sms/send`
- **Body (JSON):**

```json
{
  "to": "+1234567890",
  "message": "Este es un mensaje de prueba desde Flask."
}
```

- **Respuesta:**

```json
{
  "success": true,
  "sid": "SM1234567890abcdef"
}
```

---

## 🚀 Despliegue en Render

Si quieres poner tu API en producción, puedes desplegarla en **Render**:

1. Sube tu código a **GitHub**.
2. Ve a [Render](https://render.com/) y crea un **nuevo servicio web**.
3. Selecciona tu repo y configura las **variables de entorno**.
4. Render instalará las dependencias y ejecutará Flask automáticamente.

---

## 📝 Licencia

Este proyecto es de código abierto. ¡Úsalo como quieras! 😃

---

## 📌 Autor

🔹 **Wenzel Whilan Cruzado Villegas**  
📧 Contacto: [wenzelcruzado14@gmail.com](mailto:wenzelcruzado14@gmail.com)
