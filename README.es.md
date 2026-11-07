<div align="center">

<img src="assets/hero.svg" alt="canva-slides — skill de agente para presentaciones Canva" width="100%">

### Presentaciones Canva que resisten los límites reales de Canva

**Planificar · Construir · Verificar · Publicar** — fiel a la fuente, totalmente editable, un único enlace que nunca cambia.

[![License: MIT](https://img.shields.io/badge/license-MIT-1F5FA8)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-1F5FA8)](skills/canva-slides/SKILL.md)
[![Skill](https://img.shields.io/badge/skills-1-1F5FA8)](#estructura-del-repositorio)
[![Canva MCP + CLI](https://img.shields.io/badge/Canva-MCP%20%2B%20CLI-1F5FA8)](skills/canva-slides/references/00-preflight-and-environment.md)
[![Checked against live API](https://img.shields.io/badge/verified-live%20API-7BE0C3)](skills/canva-slides/SOURCES.md)

[English](README.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [Русский](README.ru.md) · [Français](README.fr.md) · **Español**

</div>

---

## Por qué existe

Casi todos los skills de «hazme una presentación» asumen dos cosas que suelen ser falsas:

1. **La llamada de generación con IA funciona.** No siempre: cuando se agota la cuota mensual de IA, `create-design` devuelve `quota_exceeded` al instante y reintentar no sirve de nada.
2. **Una presentación generada se puede arreglar después.** Estructuralmente no: ninguna operación de edición de Canva inserta un cuadro de texto, y el propio servicio de edición puede devolver `503` durante horas.

Este skill documenta lo que sí resistió las pruebas reales: control del plan antes de dibujar, comparación de texto con la fuente, revisión de **cada** página renderizada y una salida sin IA de Canva — construir un PPTX nativo editable en local e importarlo con la API REST oficial de Canva.

## Qué obtienes

- **Primero el plan** — hilo argumental, modo (ponente / charla / documento), títulos de acción por página, límites de palabras, cobertura de ejemplos; un linter bloquea una estructura defectuosa antes de generar.
- **Fiel a la fuente** — tabla diapositiva ↔ página para trabajos basados en un manual o PDF; los ejemplos ajenos a la fuente se etiquetan en la propia diapositiva.
- **Sistema visual, no intuiciones** — escala tipográfica en px para 1920×1080, un solo color de acento, rejilla y márgenes, lista de vetos «anti-IA», diagramas nativos.
- **Pruebas, no promesas** — diff de texto, render por página, hoja de contactos, auditoría medida de maquetación (desplazamientos, desbordes, solapamientos, zonas seguras).
- **Un enlace para siempre** — reemplazo por página vía `POST /v1/merges`; el id del diseño, el enlace y el uso compartido público sobreviven a las actualizaciones.
- **Salida nativa editable** — cuadros de texto y formas vectoriales reales en Canva, nunca imágenes a página completa.
- **Degradación progresiva** — MCP → CLI/REST → PPTX local, según lo que funcione en ese momento.
- **Vietnamita primero** — diacríticos, predicción de saltos de línea, tamaños para aula, guiones de trabajos y defensas.

## Instalación

```bash
# skills gestionados de omp
cp -R skills/canva-slides ~/.omp/agent/managed-skills/canva-slides

# cualquier agente que lea SKILL.md (Claude Code, Codex, …)
git clone https://github.com/thomas-nguyen-seamless/ai-skills-canva
cp -R ai-skills-canva/skills/canva-slides <tu-carpeta-de-skills>/
```

Después deja que el skill prepare la máquina:

```bash
skills/canva-slides/scripts/bootstrap.sh # pregunta una vez por cada herramienta ausente
skills/canva-slides/scripts/bootstrap.sh --check # solo informe, no instala nada
```

`bootstrap.sh` **solo instala lo que falta** — lo presente se muestra como `[ok] … (already installed, skipped)` y nunca se reinstala. Luego comprueba las dos cosas que no puede hacer por ti: el inicio de sesión de la CLI de Canva y el montaje MCP.

| Comprobación | Si ya existe | Si falta |
|---|---|---|
| `uv`, `python3`, `git`, `node ≥ 22`, `npx` | se informa, sin tocar | se instala con Homebrew (o el instalador oficial de `uv`) |
| CLI de Canva | se informa, no se vuelve a descargar | se obtiene una vez con `npx` (en caché, sin instalación global) |
| Librerías Python (`pillow`, `numpy`, `scipy`, `python-pptx`, `lxml`, `pymupdf`, `pypdf`) | la importación funciona → se omite | se precalientan en la caché de uv |
| Inicio de sesión de la CLI | se muestra el nombre de la cuenta | `canva login`, **tú apruebas en el navegador** |
| Montaje MCP `canva` | confirmado en `mcp.json` | se imprime el fragmento; la configuración **nunca** se sobrescribe |

## Inicio rápido

**Presentación nueva**

```text
/skill:canva-slides haz 20 diapositivas sobre «la ley de la negación de la negación»
desde @triethocmaclenin.pdf — 15 minutos, vietnamita, letra grande para el aula
```

**Editar una presentación existente manteniendo el enlace**

```bash
scripts/update_canva_deck.sh DAHaPZNNOhs deck.pptx "tmp import" --pages "5,9"
```

**Solo revisar, sin cambiar nada**

```text
/skill:canva-slides revisa esta presentación de Canva: https://canva.link/… — puntúa y lista defectos
```

## Cómo se construye una presentación

<div align="center"><img src="assets/workflow.svg" alt="Planificar, construir, verificar, publicar, exportar" width="100%"></div>

- Fase | Condición para avanzar
|---|---|---|
| 1 | **Plan** — briefing, tabla de fuentes, terminología, ficha por diapositiva, ejemplos | `plan_check.py --ghost` devuelve **0 errores** |
| 2 | **Construcción** — IA de Canva (`create-design`) *o* PPTX nativo (Arial, altura medida) | número de páginas = plan |
| 3 | **Verificación** — diff de texto, render por página, auditoría de maquetación, contraste | todas las cadenas presentes, sin fallos graves |
| 4 | **Publicación** — importar una vez y luego actualizar por página el mismo diseño | páginas correctas, enlace y uso compartido intactos |
| 5 | **Exportación** — PDF/PPTX, número de páginas verificado, notas en archivo aparte | lista de finalización completa |

## Actualizar una presentación compartida

El modo por defecto es **por página**, porque una presentación suele tener varios autores:

```bash
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --pages "5,7,12-14" # solo cambian esas páginas
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --all # todas (solo diseños propios)
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" # se niega a ejecutarse
```

Cada página son dos trabajos merge (insertar + borrar), así que el total de páginas no cambia y la numeración no se desfasa. Verificado en un diseño de 20 páginas: reemplazar la página 5 cambió **solo** la página 5 (1.266 px), las otras 19 quedaron idénticas píxel a píxel, y el id, el enlace corto y el permiso `Can view` se mantuvieron.

> La página reemplazada viene de la construcción local, así que los retoques manuales **en esa página** se pierden. Las demás no se tocan.

## Scripts

| Script | Función |
|---|---|
| `bootstrap.sh` | instala lo que falta; verifica inicio de sesión y montaje MCP |
| `plan_check.py` | linter del plan: presupuestos de palabras, títulos, duplicados, ritmo, índice, ejemplos |
| `text_diff.py` | cadenas previstas frente al texto real |
| `deck_audit.py` | auditoría medida: desplazamientos, zonas seguras, desborde, solapamiento |
| `fit_check.py` | predice saltos de línea y altura en vietnamita |
| `contrast.py` | contraste WCAG para proyección |
| `diagrams.py` | 8 tipos de diagrama al tamaño final |
| `contact_sheet.py` | una imagen con todas las páginas, numeradas |
| `post_upload.sh` | subida de recursos con URL de un solo uso |
| `update_canva_deck.sh` | sube un PPTX a un diseño existente sin cambiar id, enlace ni permisos |
| `templates/pptx-fallback/` | constructor nativo, preparación de grabados, render en PowerPoint, verificación de texto |

## Estructura del repositorio

```text
ai-skills-canva/
├── assets/ portada y diagrama del proceso
├── README.md README en 6 idiomas (EN · VI · ZH · RU · FR · ES)
└── skills/canva-slides/ un solo skill, pero profundo
 ├── SKILL.md enrutador: reglas, fases, atajos, herramientas, scripts
 ├── SOURCES.md procedencia, decisiones, registro de verificación con fechas
 ├── references/00…12 un archivo por fase
 ├── scripts/ los 10 scripts anteriores
 ├── templates/ plan.json, brief-vi, deck-rules, speaker-notes,
 │ mcp-canva.snippet.json, pptx-fallback/
 └── research/ notas de lectura de los skills estudiados
```

## Límites que el skill incorpora

| Realidad | Qué hace el skill |
|---|---|
| `create-design` / `generate-image` gastan la **cuota mensual de IA** (`quota_exceeded`, síncrono) | se detiene de inmediato, pasa a la ruta sin créditos e indica la fecha de reinicio |
| `start-editing-transaction` puede devolver `503` durante horas | degrada a lectura + exportación + merge por página; nunca afirma que un cambio quedó guardado |
| El importador PPTX de Canva pierde márgenes internos, espaciado entre párrafos y trazos freeform | un cuadro de texto por párrafo, formas simples + texto aparte, curvas como polígonos rellenos |
| Ninguna API publica ni elimina un diseño | se documentan los pasos en la interfaz, nunca se inventan comandos |
| Una presentación generada parafrasea y puede cambiar términos | diff con el plan; se corrige en el sitio, sin regenerar para arreglar texto |

Pruebas, fechas y fuentes completas: [`skills/canva-slides/SOURCES.md`](skills/canva-slides/SOURCES.md).

## Licencia

MIT — ver [LICENSE](LICENSE). Atribución de terceros en [NOTICE.md](NOTICE.md). Canva es una marca de Canva Pty Ltd; este proyecto no está afiliado ni respaldado por Canva.
