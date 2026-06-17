# README - Módulo 06: Glosario Educativo

## ¿Qué incluye este módulo?
- `glosario.md`: glosario navegable por categorías.
- `datos/glosario_datos.csv`: base estructurada de términos (50+).
- `glosario_interactivo.py`: herramienta de búsqueda y aprendizaje.
- `glosario_test.py`: validación de estructura, calidad y búsquedas.

## Cómo usar el glosario interactivo
```bash
cd 06_Glosario
python glosario_interactivo.py
```

Funciones principales:
- `buscar_término()`: encuentra un término exacto.
- `buscar_palabras_clave()`: filtra por keywords.
- `listar_por_categoría()`: muestra términos de una categoría.
- `termino_aleatorio()`: aprendizaje aleatorio.
- `similares()`: muestra términos relacionados.

## Cómo navegar el markdown
1. Abrir `glosario.md`.
2. Elegir una categoría temática.
3. Revisar definición, contexto, ejemplo, relaciones y módulo relacionado.

## Cómo contribuir nuevos términos
1. Agregar una nueva fila en `datos/glosario_datos.csv` con todos los campos.
2. Mantener la categoría consistente con las existentes.
3. Incluir contexto de uso y módulo relacionado.
4. Ejecutar:
   ```bash
   cd 06_Glosario
   python glosario_test.py
   ```

## Estructura de los términos
Campos obligatorios del CSV:
- `término`
- `categoría`
- `definición`
- `contexto`
- `ejemplo`
- `módulo_relacionado`
- `palabras_clave`

## Recursos externos recomendados
- FATF/GAFI: https://www.fatf-gafi.org/
- Pandas: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/
