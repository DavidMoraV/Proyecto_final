# Proyecto_final
# 🧠 Proyecto Final - Predicción de Diabetes (MLOps)

Este proyecto implementa un sistema de predicción de diabetes utilizando un modelo de machine learning. Está diseñado siguiendo principios de MLOps con enfoque en despliegue, automatización, validación y versionamiento.

---

## 📌 Tecnologías utilizadas

- Python 3.10
- FastAPI (API REST)
- Scikit-learn (modelo)
- Docker (contenedorización)
- GitHub Actions (CI/CD)
- DeepSource (análisis estático)
- DVC (pendiente)
- AWS S3 / EC2 (pendiente)

---

## 🚀 Cómo ejecutar la API

### ✅ Opción 1: Local (entorno virtual)

```bash
# Clonar repositorio
git clone https://github.com/DavidMoraV/Proyecto_final.git
cd Proyecto_final

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar API
uvicorn api.main:app --reload

