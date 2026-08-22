# Sensors and Actuators Laboratory — course website

Jekyll site for **25PC2RA202**, B.Tech. III Semester, CSE (Robotics & Artificial
Intelligence), VNR VJIET. Deploys on GitHub Pages with no build configuration.

Live at `https://uhvardhan.github.io/sensors-actuators-lab/`

---

## Deploy

1. Create a **new public repository** named `sensors-actuators-lab` under your account.
2. Push these files to the `main` branch.
3. Repository → **Settings** → **Pages** → Source: **Deploy from a branch** → `main` / `/ (root)`.
4. Wait for the first build (about a minute), then open the URL above.

If you name the repository something else, change `baseurl` in `_config.yml` to match —
it must be `/your-repo-name`, with a leading slash and no trailing slash. Every link on
the site is built from it, so a mismatch breaks navigation and CSS.

## Run it locally

Optional — only needed if you want to preview before pushing.

```bash
gem install bundler
bundle install
bundle exec jekyll serve --livereload
# http://127.0.0.1:4000/sensors-actuators-lab/
```

## Where things live

| I want to change… | Edit |
| --- | --- |
| Course code, outcomes, evaluation, books, instructor | `_data/course.yml` |
| The week-by-week plan and dates | `_data/schedule.yml` |
| Announcements on the home page | `_data/updates.yml` |
| The nav bar | `_data/nav.yml` |
| Institute name, logo, semester label, `baseurl` | `_config.yml` |
| An individual experiment | `_experiments/NN-slug.md` |
| Colours, type, spacing | `assets/css/style.css` |

Page bodies (`index.md`, `overview.md`, `schedule.md`, `experiments.md`, `resources.md`)
mostly pull from the data files, so in normal use you edit YAML rather than markup.

## Before you go live

- [ ] Replace `assets/images/logo-placeholder.svg` with the institute logo, and update
      `institute.logo` in `_config.yml`.
- [ ] Confirm the course code. The R25 curriculum table lists this lab as **25PC2RA202**;
      the detailed syllabus page is headed **25PC2RA203**, which is also the code printed
      on the Software Systems for Robotics and AI Laboratory. Set `code` in
      `_data/course.yml` to whichever the department confirms.
- [ ] Check the expansions of the evaluation abbreviations in `_data/course.yml` —
      D-D, PE, LR, CP are written out as day-to-day, practical examination, lab record and
      course project. Correct them if your department uses different terms.
- [ ] Fill `timings` and `venue` in `_data/course.yml` once the timetable is published.
- [ ] Fill the `date` field for each week in `_data/schedule.yml`.
- [ ] Delete the two sample entries in `_data/updates.yml`.
- [ ] Add your email to `instructors` in `_data/course.yml`, and a photo if you want one.

## Adding an experiment sheet

Drop the PDF in `assets/files/`, then in the experiment's front matter:

```yaml
status: released
resources:
  - name: Experiment sheet (PDF)
    url: /assets/files/exp01.pdf
```

`status: released` turns the grey status dot on the experiment page green.

## Adding an update

Newest first in `_data/updates.yml`:

```yaml
- date: "12 Sep"
  body: >-
    Experiment 3 datasets are on the [Resources](/resources/) page.
```

Write internal links starting with `/` — the layout rewrites them to include `baseurl`.

## Structure

```
_config.yml           site config, institute block, collection setup
_data/                course.yml, schedule.yml, updates.yml, nav.yml
_experiments/         one markdown file per experiment (collection)
_layouts/             default, page, home, experiment
_includes/            head, masthead, nav, footer
assets/css/style.css  all styling, no framework
assets/images/        logo and favicon
assets/files/         experiment sheets and datasets
```

## Notes on the design

Two accent colours carry meaning rather than decoration: teal marks Cycle I (sensing),
ochre marks Cycle II (actuation). The gradient strip under the masthead runs teal to ochre
across the width of the page — the shape of the course in one line. Experiment numbers are
set in tabular monospace so they align down a column like readings on an instrument.

Typography is IBM Plex — Condensed for headings, Sans for body, Mono for codes, numbers and
labels. It was drawn for technical documentation, which is what this is.
