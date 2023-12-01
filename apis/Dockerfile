# Utiliza la imagen oficial de Python
FROM python:3.12.0-bookworm

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Expone el puerto 5000, que es el puerto predeterminado para Flask
EXPOSE 5000

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py

# Ejecuta la aplicación cuando se inicie el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]