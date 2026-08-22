`vnrvjiet-logo.svg` is the official VNR VJIET emblem (the dotted arch), redrawn as vector
circles so it stays sharp at any size. `favicon.svg` is the same emblem on the site's ink
square. `institute.logo` in `_config.yml` points at the former; `_includes/head.html` points
at the latter.

The emblem's natural aspect ratio is 120:81 — size it by width and leave `height: auto`.
`logo-placeholder.svg` is the old stand-in and is no longer referenced; safe to delete.

Instructor photos go here too — set `instructors[].photo` in `_data/course.yml` to
`/assets/images/your-photo.jpg`.
