# Instrucciones para Clonar e Instalar el Proyecto

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd back-testcases
```

## 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 4. Aplicar migraciones de la base de datos

```bash
python manage.py migrate
```

## 5. Crear un superusuario (opcional, para acceder al admin de Django)

```bash
python manage.py createsuperuser
```

## 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

## 7. Acceso
- Panel de administración: http://localhost:8000/admin/
- Documentación de la API (si está habilitada): http://localhost:8000/swagger/ o http://localhost:8000/redoc/

---

**Nota:**
- Asegúrate de tener Python 3.8 o superior instalado.
- Si usas base de datos PostgreSQL, configura las variables de entorno en `core/settings/local.py` según tus credenciales.
