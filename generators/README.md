# ElianaTech Social Media Content Generators

Python scripts for generating social media content for ElianaTech.

## LinkedIn Content Generator

Generates LinkedIn posts in multiple formats.

```bash
# Single topic with default format (thought-leadership)
python linkedin-content-generator.py --topic "Cloud Migration"

# Specific format
python linkedin-content-generator.py --topic "AI Strategy" --format how-to

# Promote a blog article
python linkedin-content-generator.py --topic "Kubernetes" --format blog-promotion \
  --blog-title "K8s Best Practices" --blog-url "https://elianatech.com/blog/k8s"

# Multiple variations
python linkedin-content-generator.py --topic "Cybersecurity" --variations 5

# Interactive mode
python linkedin-content-generator.py --interactive
```

**Formats:** thought-leadership, how-to, listicle, story, blog-promotion

## Instagram Content Generator

Generates Instagram posts with captions and visual design briefs.

```bash
# Single image post
python instagram-content-generator.py --topic "Cloud Computing"

# Carousel (multi-slide)
python instagram-content-generator.py --topic "AI Trends" --format carousel --slides 8

# Story series
python instagram-content-generator.py --topic "Cybersecurity" --format story

# Reel concept with script
python instagram-content-generator.py --topic "DevOps" --format reel

# Generate all formats at once
python instagram-content-generator.py --topic "Data Analytics" --format all

# Content calendar for 4 weeks
python instagram-content-generator.py --calendar 4

# Export to JSON
python instagram-content-generator.py --topic "AI" --format all --export-json

# Interactive mode
python instagram-content-generator.py --interactive
```

**Formats:** single, carousel, story, reel, all

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)
