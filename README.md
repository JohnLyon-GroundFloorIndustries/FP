# Flora Pacifica — website design preview

A static design preview of a website for Flora Pacifica, a wedding floral design studio serving Washington and the Pacific Northwest. It is published with GitHub Pages from the `docs/` folder.

**Live site:** https://johnlyon-groundfloorindustries.github.io/FP/

## What this is, and is not

- **A design preview.** 18 static pages with images, styles and a small menu script. No build step.
- **Not the server application.** There is no inquiry form, no message sending, no analytics and no staff or client login. Inquiry buttons link to https://florapacifica.co/contact.
- **Public, but asks not to be indexed.** Every page carries a `noindex` request for search engines. That is a request, not access control: anyone with the link can open the site.
- **Not yet cleared as the business website.** Confirm the copy and image rights before using it as Flora Pacifica's public site.

## Pages

| Page | Path |
| --- | --- |
| Home | `docs/index.html` |
| The studio | `docs/studio/` |
| Approach | `docs/approach/` |
| Commissions | `docs/commissions/` |
| Private inquiry | `docs/inquiry/` |
| Selected work, with five celebrations | `docs/work/` |
| Journal, with three articles | `docs/journal/` |
| Privacy and Accessibility | `docs/privacy/`, `docs/accessibility/` |
| Not found | `docs/404.html` |

## Files

| File | Purpose |
| --- | --- |
| `docs/` | The published site: pages, `images/`, `assets/` (`site.css`, `menu.js`), `favicon.svg`, `sitemap.xml`, `.nojekyll`. |
| `START-HERE.txt` | The original upload and publishing instructions that came with the package. |
| `VERIFICATION.json`, `BROWSER_TESTS.json` | Checks recorded when the package was built: page and link counts, and layout tests at desktop and phone widths. They predate publishing, so `VERIFICATION.json` still says the GitHub deployment was not performed. |
| `desktop-preview.png`, `mobile-preview.png`, `mobile-inquiry.png` | Full-page screenshots of the design. |

## Viewing and updating

- GitHub Pages serves the `docs/` folder of the `main` branch. Edit files under `docs/` and push to `main`; the live site updates within a minute or two.
- **The `/FP/` path is built into every link, image and stylesheet address.** The pages display correctly only when served at that path, so review changes on the live site; opening `docs/index.html` straight from disk shows the page without its styles or images.
- Renaming the repository, adding a custom domain or moving the site to a root address means regenerating those addresses and the metadata. No `CNAME` file is included.
