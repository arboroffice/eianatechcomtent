# ElianaTech.com — Content Plan & Generators

Content strategy, editorial calendar, and social media content generators for [elianatech.com](https://elianatech.com).

## Documents

| File | Description |
|------|-------------|
| [CONTENT-PLAN.md](./CONTENT-PLAN.md) | Master content strategy — goals, audience, site pages, workflow |
| [SITE-STRUCTURE.md](./SITE-STRUCTURE.md) | Information architecture, sitemap, URL structure, templates |
| [BLOG-CALENDAR.md](./BLOG-CALENDAR.md) | 6-month editorial calendar with topics, keywords, and pillars |
| [SEO-STRATEGY.md](./SEO-STRATEGY.md) | Keyword research, on-page SEO, technical SEO, link building |

## Social Media Generators

| Tool | Description |
|------|-------------|
| [LinkedIn Generator](./generators/linkedin-content-generator.py) | Generate LinkedIn posts in 5 formats |
| [Instagram Generator](./generators/instagram-content-generator.py) | Generate IG posts, carousels, stories, and reels |

See [generators/README.md](./generators/README.md) for usage instructions.

## Quick Start

```bash
# Generate a LinkedIn post
python generators/linkedin-content-generator.py --topic "Cloud Migration" --format thought-leadership

# Generate an Instagram carousel
python generators/instagram-content-generator.py --topic "AI Trends" --format carousel

# Interactive mode
python generators/linkedin-content-generator.py --interactive
python generators/instagram-content-generator.py --interactive
```
