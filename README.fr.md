<div align="center">

<img src="assets/hero.svg" alt="canva-slides — compétence d'agent pour présentations Canva" width="100%">

### Des présentations Canva qui résistent aux vraies limites de Canva

**Planifier · Construire · Vérifier · Publier** — fidèle à la source, entièrement modifiable, un seul lien qui ne change jamais.

[![License: MIT](https://img.shields.io/badge/license-MIT-1F5FA8)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-1F5FA8)](skills/canva-slides/SKILL.md)
[![Skill](https://img.shields.io/badge/skills-1-1F5FA8)](#structure-du-dépôt)
[![Canva MCP + CLI](https://img.shields.io/badge/Canva-MCP%20%2B%20CLI-1F5FA8)](skills/canva-slides/references/00-preflight-and-environment.md)
[![Checked against live API](https://img.shields.io/badge/verified-live%20API-7BE0C3)](skills/canva-slides/SOURCES.md)

[English](README.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [Русский](README.ru.md) · **Français** · [Español](README.es.md)

</div>

---

## Pourquoi cette compétence existe

La plupart des compétences « fais-moi une présentation » reposent sur deux hypothèses souvent fausses :

1. **L'appel de génération IA fonctionne.** Non : quand le quota IA mensuel est épuisé, `create-design` renvoie immédiatement `quota_exceeded`, et réessayer ne sert à rien.
2. **Une présentation générée peut être réparée ensuite.** Pas structurellement : aucune opération d'édition Canva n'ajoute de zone de texte, et le service d'édition lui-même peut renvoyer `503` pendant des heures.

Cette compétence consigne ce qui a tenu en conditions réelles : un contrôle du plan avant toute production, une comparaison texte par texte avec la source, l'examen de **chaque** page rendue, et une solution de repli sans IA Canva — construire localement un PPTX natif modifiable et l'importer via l'API d'import REST officielle de Canva.

## Ce que vous obtenez

- **Entretien de design d'abord** — avant de construire, un questionnaire adapté au sujet (thème, densité, langage visuel, images, citations, diapositives spéciales) ; les réponses vont dans le plan et le linter bloque tant qu'elles manquent.
- **Le plan d'abord** — fil conducteur, mode (orateur / exposé / document), titres affirmatifs par page, limites de mots, couverture des exemples ; un linter bloque une structure fautive avant génération.
- **Fidèle à la source** — tableau de correspondance page de slide ↔ page du document pour un support de cours ou un PDF ; les exemples hors source sont signalés sur la diapositive.
- **Un système visuel, pas des impressions** — échelle typographique en px pour 1920×1080, un seul accent, grille et marges, liste d'interdits « anti-effet IA », schémas natifs.
- **Des preuves, pas des promesses** — diff de texte, rendu page par page, planche contact, audit mesuré de la mise en page (décalages, débordements, chevauchements, zones de sécurité).
- **Un lien pour toujours** — remplacement page par page via `POST /v1/merges` ; l'id du design, le lien et le partage public survivent aux mises à jour.
- **Rendu natif modifiable** — vraies zones de texte et formes vectorielles dans Canva, jamais des images pleine page.
- **Dégradation progressive** — MCP → CLI/REST → PPTX local, selon ce qui fonctionne à l'instant donné.
- **Vietnamien d'abord** — diacritiques, prédiction des retours à la ligne, tailles pour l'amphi, scénarios de mémoire et de soutenance.

## Installation

```bash
# compétences gérées par omp
cp -R skills/canva-slides ~/.omp/agent/managed-skills/canva-slides

# tout agent qui lit SKILL.md (Claude Code, Codex, …)
git clone https://github.com/thomas-nguyen-seamless/ai-skills-canva
cp -R ai-skills-canva/skills/canva-slides <votre-dossier-de-compétences>/
```

Puis laissez la compétence préparer la machine :

```bash
skills/canva-slides/scripts/bootstrap.sh # demande une fois par outil manquant
skills/canva-slides/scripts/bootstrap.sh --check # rapport seul, aucune installation
```

`bootstrap.sh` **n'installe que ce qui manque** — ce qui est présent s'affiche `[ok] … (already installed, skipped)` et n'est jamais réinstallé. Il vérifie ensuite les deux choses qu'il ne peut pas faire à votre place : la connexion à la CLI Canva et le montage MCP.

| Vérifié | Si présent | Si absent |
|---|---|---|
| `uv`, `python3`, `git`, `node ≥ 22`, `npx` | signalé, intact | installé via Homebrew (ou l'installeur officiel pour `uv`) |
| CLI Canva | signalé, non retéléchargé | récupéré une fois via `npx` (en cache, sans installation globale) |
| Bibliothèques Python (`pillow`, `numpy`, `scipy`, `python-pptx`, `lxml`, `pymupdf`, `pypdf`) | import OK → ignoré | préchargées dans le cache uv |
| Connexion CLI Canva | nom du compte affiché | `canva login`, **vous validez dans le navigateur** |
| Montage MCP `canva` | confirmé dans `mcp.json` | extrait affiché ; la configuration n'est **jamais** écrasée |

## Démarrage rapide

**Nouvelle présentation**

```text
/skill:canva-slides fais 20 diapos sur « la loi de la négation de la négation »
depuis @triethocmaclenin.pdf — 15 minutes, vietnamien, grands caractères pour l'amphi
```

**Modifier une présentation existante en gardant le lien**

```bash
scripts/update_canva_deck.sh DAHaPZNNOhs deck.pptx "tmp import" --pages "5,9"
```

**Relire seulement, sans rien changer**

```text
/skill:canva-slides évalue cette présentation Canva : https://canva.link/… — note et liste les défauts
```

## Comment un deck se construit

<div align="center"><img src="assets/workflow.svg" alt="Planifier, construire, vérifier, publier, exporter" width="100%"></div>

| # | Étape | Condition pour avancer |
|---|---|---|
| 1 | **Plan** — brief, tableau des sources, terminologie, fiche par diapo, exemples | `plan_check.py --ghost` renvoie **0 erreur** |
| 2 | **Construction** — IA Canva (`create-design`) *ou* PPTX natif (Arial, hauteur mesurée) | nombre de pages = plan |
| 3 | **Vérification** — diff de texte, rendu page par page, audit de mise en page, contraste | toutes les chaînes présentes, aucun défaut bloquant |
| 4 | **Publication** — import unique, puis mises à jour page par page du même design | pages conformes, lien et partage intacts |
| 5 | **Export** — PDF/PPTX, nombre de pages vérifié, notes en fichier séparé | liste de fin de mission cochée |

## Mettre à jour une présentation partagée

Le mode par défaut est **page par page**, car un deck a souvent plusieurs auteurs :

```bash
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --pages "5,7,12-14" # seules ces pages changent
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --all # toutes les pages (deck solo)
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" # refuse de s'exécuter
```

Deux tâches merge par page (insertion + suppression) gardent le nombre de pages constant : la numérotation ne dérive jamais. Vérifié sur un design de 20 pages : remplacer la page 5 ne modifie **que** la page 5 (1 266 px), les 19 autres sont identiques au pixel près ; l'id, le lien court et le partage `Can view` sont conservés.

> Une page remplacée vient de la construction locale : les retouches manuelles **sur cette page** sont perdues. Les autres pages ne sont pas touchées.

## Scripts

| Script | Rôle |
|---|---|
| `bootstrap.sh` | installe ce qui manque ; vérifie connexion et montage MCP |
| `intake_prompt.py` | questionnaire de design généré à partir du sujet |
| `plan_check.py` | linter du plan : budgets de mots, titres, doublons, rythme, sommaire, exemples |
| `text_diff.py` | chaînes prévues vs texte réel |
| `deck_audit.py` | audit mesuré : décalages, zones de sécurité, débordement, chevauchement |
| `fit_check.py` | prédit les retours à la ligne et la hauteur en vietnamien |
| `contrast.py` | contraste WCAG pour la projection |
| `diagrams.py` | 8 types de schémas à la taille finale |
| `contact_sheet.py` | une image de toutes les pages, numérotées |
| `post_upload.sh` | envoi d'un média via une URL à usage unique |
| `update_canva_deck.sh` | pousse un PPTX dans un design existant sans changer id, lien ni partage |
| `templates/pptx-fallback/` | constructeur natif, préparation des gravures, rendu PowerPoint, vérification du texte |

## Structure du dépôt

```text
ai-skills-canva/
├── assets/ bannière et schéma de processus
├── README.md README en 6 langues (EN · VI · ZH · RU · FR · ES)
└── skills/canva-slides/ une compétence, mais profonde
 ├── SKILL.md routeur : règles, phases, raccourcis, outils, scripts
 ├── SOURCES.md provenance, arbitrages, journal de vérification daté
 ├── references/00…12 un fichier par phase
 ├── scripts/ les 10 scripts ci-dessus
 ├── templates/ plan.json, brief-vi, deck-rules, speaker-notes,
 │ mcp-canva.snippet.json, pptx-fallback/
 └── research/ notes de lecture sur les compétences étudiées
```

## Limites encodées dans la compétence

| Réalité | Ce que fait la compétence |
|---|---|
| `create-design` / `generate-image` consomment le **quota IA mensuel** (`quota_exceeded`, synchrone) | s'arrête aussitôt, bascule sur le parcours sans crédits, indique la date de réinitialisation |
| `start-editing-transaction` peut renvoyer `503` pendant des heures | passe en lecture + export + merge page par page ; ne prétend jamais qu'une modification est enregistrée |
| L'import PPTX de Canva perd les marges internes, l'espacement des paragraphes et les traits freeform | une zone de texte par paragraphe, formes simples + texte séparé, courbes en polygones remplis |
| Aucune API ne rend un design public ni ne le supprime | étapes d'interface documentées, jamais de commande inventée |
| Un deck généré paraphrase et peut remplacer des termes | diff avec le plan ; correction sur place, jamais de régénération pour corriger le texte |

Preuves, dates et sources : [`skills/canva-slides/SOURCES.md`](skills/canva-slides/SOURCES.md).

## Licence

MIT — voir [LICENSE](LICENSE). Attribution tierce dans [NOTICE.md](NOTICE.md). Canva est une marque de Canva Pty Ltd ; ce projet n'y est ni affilié ni approuvé.
