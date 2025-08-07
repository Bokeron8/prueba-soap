
# Proyecto: Cliente SOAP para ModuloParadas

Este repositorio contiene dos programas que consumen un servicio SOAP del sistema **ModuloParadas** para recuperar información de líneas según localidad.

* **PHP:** usa `SoapClient` para llamar al servicio SOAP.
* **Python:** usa la librería [`zeep`](https://docs.python-zeep.org/en/master/) para consumir el mismo servicio.


---

## Requisitos

### PHP

* PHP >= 7.2 con extensión SOAP (`php-soap`)
* Composer (para instalar dependencias)

### Python

* Python 3.6+
* Librerías indicadas en `requirements.txt` (`zeep`, `python-dotenv`)

---

## Instalación

### PHP

1. Instalar dependencias con Composer:

```bash
composer install
```

2. Asegurarse de que la extensión SOAP esté habilitada en PHP.

### Python

1. Crear un entorno virtual (opcional pero recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Uso

### PHP

Ejecutar el script PHP desde consola:

```bash
php index.php
```

Asegurarse que el archivo `.env` esté configurado si usás variables de entorno para credenciales.

---

### Python

Ejecutar el script Python:

```bash
python main.py
```

Asegurarse que el archivo `.env` esté configurado si usás variables de entorno para credenciales.

---

## Variables de entorno

Para no exponer credenciales, se recomienda usar un archivo `.env` con las siguientes variables:

```
USUARIO=UNUSUARIO
CLAVE=LACLAVE
```

---
