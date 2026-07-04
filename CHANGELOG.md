# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Fase 2.1 (ROADMAP-ANTI-IA): differentiated the opening mold by page type — the 8 area leads now open with the client's concrete situation/consequence, with the firm's action statement following (previously always firm-first); the 7 profile heroes now open with portrait + a verifiable biographical fact (graduation and OAB admission year) before the practice-area summary (previously text-only, service-list first); escritorio.html already opened with the 1989 founding fact (verified, no change needed).
- Fixed two ADR-006/007 violations found while touching page-hero CSS, missed by the original sweep: a decorative wash gradient on `.hero::after`/`.page-hero::after` in all three page CSS files (home, area-societario, profissionais), and the internal-page h1 (index's own hero h1 had already been fixed in PR #1) still using weight 300 / non-standard tracking instead of the ADR-007 display parameters (360/−0.045em/0.96).
- Fase 2.2 (ROADMAP-ANTI-IA): removed leftover decorative roman-numeral markers (`class="number"`) from the 8 area pages, escritorio and all 8 profile pages; removed eyebrows fully redundant with an adjacent h2 (Trajetória, Atuação institucional, Visão geral, Equipe, Experiência representativa) and the site-wide, information-free "Síntese" hero label; preserved eyebrows that are the sole orientation for a content block (Como atuamos, Temas correlatos, Publicações relacionadas) or name genuinely distinct categories (index.html sections; Sócios / Sócias e equipe).
- preflight: fixed F4 double-counting the same visual label (section-label wrapper + inner eyebrow span); added a documented per-page exception list (EXCECOES_F4) for cases where the label informs rather than decorates (ADR-010 test), replacing the generic --tolerar F4 used since Fase 0; extended F6 to flag any remaining decorative roman numerals.
- Fase 1 editorial pass (12_fonte ban-list) on index, escritorio and the 8 practice-area pages: decorative triads and antithesis scaffolds rewritten, "altamente" removed, the leaked internal editorial guideline in the Publicações heading replaced, and the uniform "Discutir uma demanda em [área]" CTA reformulated as one concrete client question per area.
- Replaced all 58 `<image-slot>` mockup placeholders with real `<img>` elements (descriptive alt, intrinsic width/height, lazy loading below the fold) and deleted `assets/js/image-slot.js` (Fase 0.1 of ROADMAP-ANTI-IA; templates-npm ADR-009).
- Removed the decorative PT/EN language toggle and its CSS until an English version exists (Fase 0.2).
- Added `scripts/preflight.py` with a `--tolerar` flag and a GitHub Actions workflow running it on pushes and PRs (F4 tolerated as declared Fase 2 debt).
- `assets/css/identidade.css` with the signature element (linha de autuação, per templates-npm ADR-011): a mono metadata line atop each page title with page-specific verifiable data and the constant "DESDE 1989" closure, replacing decorative numbering (page-hero "NPM"/"Área 0X" markers, index card numbers, roman section numerals).
- `assets/css/tokens.css` as the single visual-token source aligned with the `templates-npm` V8.2.9 identity (ink/navy palette, warm paper surfaces, display parameters).
- `contato.html` with a Netlify Forms contact form, LGPD notice, and office contact data.
- `_redirects` mapping all legacy Wix URLs (practice-area slugs, `/areas-de-atuacao`, `/blog`, `/contato`) to the new site with 301s.

- `areas/tributario.html` as the v1 tax practice page.
- `areas/contratual.html` as the v1 contract law practice page.
- `areas/arbitragem.html` as the v1 arbitration and mediation page.
- `areas/imobiliario.html` as the v1 real estate practice page.
- `areas/patrimonial-sucessorio.html` as the v1 wealth and succession planning page.
- `areas/contencioso-civel.html` as the v1 civil litigation page.
- `areas/familia-sucessoes.html` as the v1 family and succession page.
- Individual profile pages for `Fábio Plantulli`, `André Manzoli`, `Thaís de Vilhena Moraes Silva`, `Tathiana da Fonseca Fiuza Dittmers`, `Iago Pires Garcia`, and `Paola de Oliveira Giannotti`.
- `robots.txt`, `sitemap.xml`, and `404.html` as the minimum technical publication layer for the v1 site.
- `AUDITORIA-PROJETO-V1.md` with a publication-readiness review of the repository and site scope.
- `MATRIZ-INTERNA-AREAS-EQUIPE.md` as the internal editorial rule for associating professionals with practice areas.

### Changed

- Updated the home page so the tax and contract practice cards point to real internal pages.
- Updated the home page so all eight practice-area cards now point to real internal pages.
- Updated the home page and team page so individual professional cards and names point to real profile pages.
- Expanded `escritorio.html` with a stronger institutional-positioning section grounded in the support reports and folder.
- Replaced em dashes with en dashes across the active site base, governance documents, and text-based assets for typographic consistency.
- Added meta descriptions, canonical links, Open Graph tags, and favicon references across the active public pages.
- Aligned the legal pages with the official office navigation and softened temporary labels to a more publication-ready institutional wording.
- Updated project documentation to reflect that `escritorio.html` is already part of the active v1 base.
- Updated the roadmap status to show Sprint 2 as complete and Sprint 3 as in progress.

### Planned

- Create the remaining area pages for the v1 sitemap.
- Create the remaining individual professional profile pages.
- Add technical publication assets for deploy readiness, including metadata, sitemap, and robots instructions.

## [0.1.0] - 2026-06-10

### Added

- Canonical home page in `index.html`.
- Base page for the corporate law practice in `areas/societario.html`.
- Team listing page in `profissionais/index.html`.
- First individual profile page in `profissionais/luiz-novaes.html`.
- Shared CSS and JS asset structure under `assets/`.
- Institutional privacy and cookies pages.
- Project roadmap, site structure guide, Sprint 2 scope document, and v1 content matrix.
- Anti-drift governance document for editorial, structural, and versioning consistency.
- Git repository initialization, remote connection, and first published history.

### Changed

- Rewrote institutional positioning to align more closely with the office folder and validated public references.
- Reorganized the project so the active site base is separated from raw source materials and historical mockups.
- Standardized names, image paths, and active project structure.

### Deprecated

- Historical HTML mockups are no longer the base for ongoing evolution.

### Removed

- Legacy and raw-reference materials from the active versioned core of the project.
