#!/usr/bin/env python3
"""
ElianaTech Instagram Photo Content Generator

Generates Instagram post content including:
- Caption text with hashtags
- Visual design briefs / specifications for photo/graphic creation
- Carousel slide outlines
- Story content ideas

Supports formats: single post, carousel, story, reel concept.

Usage:
    python instagram-content-generator.py --topic "Cloud Computing"
    python instagram-content-generator.py --topic "AI Trends" --format carousel
    python instagram-content-generator.py --interactive
"""

import argparse
import random
import textwrap
import json
from datetime import datetime


# ──────────────────────────────────────────────────────────────
# Brand Design System
# ──────────────────────────────────────────────────────────────

BRAND = {
    "name": "ElianaTech",
    "handle": "@elianatech",
    "colors": {
        "primary": "#0A2463",       # Deep navy blue
        "secondary": "#3E92CC",     # Bright blue
        "accent": "#2EC4B6",        # Teal/cyan
        "highlight": "#FF6B35",     # Orange accent
        "dark": "#1B1B2F",          # Near-black
        "light": "#F7F7FF",         # Off-white
    },
    "fonts": {
        "heading": "Inter Bold / Montserrat Bold",
        "body": "Inter Regular / Open Sans",
        "accent": "Space Mono (for code snippets)",
    },
    "style_notes": [
        "Clean, modern, minimalist aesthetic",
        "Use gradients sparingly (navy to teal)",
        "Tech-inspired geometric patterns as backgrounds",
        "Code snippets in dark theme when applicable",
        "Always include ElianaTech logo watermark",
        "Consistent padding: 40px margins on all sides",
    ],
}


# ──────────────────────────────────────────────────────────────
# Caption Templates
# ──────────────────────────────────────────────────────────────

CAPTION_TEMPLATES = {
    "tip": [
        textwrap.dedent("""\
            💡 Quick {topic} tip:

            {tip_text}

            Save this for later and share with your team.

            ─────
            Follow @elianatech for daily tech insights.
            🔗 Link in bio for more.

            {hashtags}"""),
        textwrap.dedent("""\
            Here's something most people get wrong about {topic}:

            {tip_text}

            Double tap if this was helpful ❤️

            ─────
            @elianatech | Building better technology.

            {hashtags}"""),
    ],
    "carousel": [
        textwrap.dedent("""\
            Swipe through our guide to {topic} →

            What you'll learn:
            {slide_summary}

            Save this post and share it with someone who needs it 📌

            ─────
            Follow @elianatech for more tech breakdowns.

            {hashtags}"""),
        textwrap.dedent("""\
            {topic} explained in {slide_count} slides 👇

            We broke it down so you don't have to.

            Save ✅ Share ↗️ Follow for more.

            ─────
            @elianatech | Tech, simplified.

            {hashtags}"""),
    ],
    "quote": [
        textwrap.dedent("""\
            "{quote_text}"

            {attribution}

            What's your take on this? 👇

            ─────
            @elianatech

            {hashtags}"""),
    ],
    "stat": [
        textwrap.dedent("""\
            {stat_number}

            {stat_context}

            The data doesn't lie. {topic} is reshaping the industry.

            ─────
            Follow @elianatech for data-driven tech insights.

            {hashtags}"""),
    ],
    "behind-the-scenes": [
        textwrap.dedent("""\
            Behind the scenes at ElianaTech 👀

            {bts_description}

            This is what building great technology looks like.

            ─────
            Want to join the team? Link in bio.

            {hashtags}"""),
    ],
}


# ──────────────────────────────────────────────────────────────
# Visual Design Brief Templates
# ──────────────────────────────────────────────────────────────

SINGLE_POST_DESIGNS = [
    {
        "layout": "Centered text on gradient background",
        "background": "Linear gradient from {primary} to {accent}",
        "text_area": "Large heading centered, body text below",
        "elements": ["Logo watermark bottom-right", "Subtle geometric pattern overlay"],
        "dimensions": "1080x1080px (square)",
    },
    {
        "layout": "Split layout — text left, icon/illustration right",
        "background": "Solid {dark} with {accent} accent line",
        "text_area": "Left 60% for text, right 40% for visual",
        "elements": ["Tech icon or illustration", "Logo bottom-center"],
        "dimensions": "1080x1080px (square)",
    },
    {
        "layout": "Bold stat with context",
        "background": "Solid {primary} with subtle dot grid pattern",
        "text_area": "Large number/stat top, explanation text bottom",
        "elements": ["Highlight color for the stat number", "Source citation small text"],
        "dimensions": "1080x1080px (square)",
    },
    {
        "layout": "Quote card",
        "background": "{dark} with {accent} quotation marks",
        "text_area": "Quote centered with attribution below",
        "elements": ["Large decorative quotation marks", "Author photo circle (if available)"],
        "dimensions": "1080x1080px (square)",
    },
]

CAROUSEL_SLIDE_TEMPLATES = {
    "cover": {
        "layout": "Title slide",
        "elements": ["Post title (large, bold)", "Subtitle or hook text", "Swipe arrow indicator", "Logo"],
        "background": "Gradient {primary} to {secondary}",
    },
    "content": {
        "layout": "Content slide",
        "elements": ["Slide number (top-left)", "Heading", "2-3 bullet points or short paragraph", "Icon or small illustration"],
        "background": "Solid {dark} or {light} (alternate)",
    },
    "closing": {
        "layout": "CTA slide",
        "elements": ["Follow CTA", "@elianatech handle", "Logo", "Website URL"],
        "background": "Gradient {secondary} to {accent}",
    },
}


# ──────────────────────────────────────────────────────────────
# Hashtag Sets
# ──────────────────────────────────────────────────────────────

HASHTAG_SETS = {
    "cloud": "#CloudComputing #AWS #Azure #GCP #DevOps #CloudMigration #Infrastructure #TechTips #ElianaTech #Technology",
    "ai": "#AI #ArtificialIntelligence #MachineLearning #DeepLearning #GenerativeAI #TechTrends #ElianaTech #Innovation #FutureTech #DataScience",
    "security": "#CyberSecurity #InfoSec #DataSecurity #ZeroTrust #Hacking #TechSecurity #ElianaTech #DigitalSecurity #AppSec #Privacy",
    "development": "#SoftwareDevelopment #Coding #Programming #WebDev #CleanCode #DevLife #ElianaTech #TechCommunity #Developer #CodeTips",
    "data": "#DataAnalytics #DataEngineering #BigData #DataScience #SQL #DataPipelines #ElianaTech #Analytics #TechData #BusinessIntelligence",
    "general": "#Technology #DigitalTransformation #TechTips #Innovation #ElianaTech #StartupLife #TechCommunity #FutureTech #BusinessTech #TechStrategy",
}


# ──────────────────────────────────────────────────────────────
# Content Topic Ideas Library
# ──────────────────────────────────────────────────────────────

TOPIC_IDEAS = {
    "cloud": [
        {"title": "5 Cloud Cost Optimization Hacks", "type": "carousel"},
        {"title": "Cloud Migration Checklist", "type": "carousel"},
        {"title": "AWS vs Azure vs GCP at a Glance", "type": "carousel"},
        {"title": "Serverless: When to Use It", "type": "single"},
        {"title": "Cloud spending stat of the week", "type": "stat"},
    ],
    "ai": [
        {"title": "AI Use Cases That Actually Work", "type": "carousel"},
        {"title": "LLM vs Traditional ML: Quick Guide", "type": "carousel"},
        {"title": "AI Myth vs Reality", "type": "carousel"},
        {"title": "Prompt Engineering Tips", "type": "carousel"},
        {"title": "AI adoption stat", "type": "stat"},
    ],
    "security": [
        {"title": "Your Security Checklist for 2026", "type": "carousel"},
        {"title": "Zero Trust in 60 Seconds", "type": "single"},
        {"title": "Top 5 Vulnerabilities to Watch", "type": "carousel"},
        {"title": "Data breach stat", "type": "stat"},
        {"title": "Security Tip of the Week", "type": "single"},
    ],
    "development": [
        {"title": "Clean Code Principles", "type": "carousel"},
        {"title": "Git Commands Every Dev Needs", "type": "carousel"},
        {"title": "API Design Do's and Don'ts", "type": "carousel"},
        {"title": "Code Review Best Practices", "type": "carousel"},
        {"title": "Dev productivity tip", "type": "single"},
    ],
    "data": [
        {"title": "Data Pipeline Architecture Patterns", "type": "carousel"},
        {"title": "SQL vs NoSQL Decision Guide", "type": "carousel"},
        {"title": "Data Quality Checklist", "type": "carousel"},
        {"title": "Data governance stat", "type": "stat"},
        {"title": "Analytics Tip of the Week", "type": "single"},
    ],
}


# ──────────────────────────────────────────────────────────────
# Core Generation Functions
# ──────────────────────────────────────────────────────────────

def detect_category(topic: str) -> str:
    """Detect content category from topic string."""
    topic_lower = topic.lower()
    if any(w in topic_lower for w in ["cloud", "aws", "azure", "gcp", "infrastructure", "kubernetes"]):
        return "cloud"
    if any(w in topic_lower for w in ["ai", "machine learning", "ml", "llm", "neural", "deep learning"]):
        return "ai"
    if any(w in topic_lower for w in ["security", "cyber", "breach", "zero trust", "soc"]):
        return "security"
    if any(w in topic_lower for w in ["software", "code", "develop", "api", "frontend", "backend"]):
        return "development"
    if any(w in topic_lower for w in ["data", "analytics", "pipeline", "database", "sql"]):
        return "data"
    return "general"


def generate_single_post(topic: str) -> dict:
    """Generate a single Instagram post with caption and design brief."""
    category = detect_category(topic)
    hashtags = HASHTAG_SETS.get(category, HASHTAG_SETS["general"])
    design = random.choice(SINGLE_POST_DESIGNS)

    # Pick a caption template
    template_type = random.choice(["tip", "quote", "stat"])
    templates = CAPTION_TEMPLATES.get(template_type, CAPTION_TEMPLATES["tip"])
    caption_template = random.choice(templates)

    placeholders = {
        "topic": topic,
        "hashtags": hashtags,
        "tip_text": f"When implementing {topic.lower()}, always start with a clear objective. The technology is the easy part — alignment is what makes or breaks the project.",
        "quote_text": f"The best technology is the one that solves real problems for real people.",
        "attribution": "— ElianaTech",
        "stat_number": f"{random.choice(['73%', '85%', '60%', '92%', '3x', '10x'])}",
        "stat_context": f"of companies that invest in {topic.lower()} report significant improvements within the first year.",
        "bts_description": f"Our team diving deep into a {topic.lower()} project this week.",
        "slide_count": "5",
        "slide_summary": "",
    }

    caption = caption_template.format(**placeholders)

    # Format design brief with brand colors
    formatted_design = {}
    for key, value in design.items():
        if isinstance(value, str):
            formatted_design[key] = value.format(**BRAND["colors"])
        elif isinstance(value, list):
            formatted_design[key] = [v.format(**BRAND["colors"]) if isinstance(v, str) else v for v in value]
        else:
            formatted_design[key] = value

    return {
        "type": "single_post",
        "topic": topic,
        "caption": caption,
        "design_brief": formatted_design,
        "brand_colors": BRAND["colors"],
        "fonts": BRAND["fonts"],
        "style_notes": BRAND["style_notes"],
    }


def generate_carousel(topic: str, num_slides: int = 7) -> dict:
    """Generate an Instagram carousel with slides and design briefs."""
    category = detect_category(topic)
    hashtags = HASHTAG_SETS.get(category, HASHTAG_SETS["general"])

    # Generate slide content
    slides = []

    # Cover slide
    slides.append({
        "slide_number": 1,
        "type": "cover",
        "heading": topic,
        "subheading": "A quick guide by ElianaTech",
        "design": {k: v.format(**BRAND["colors"]) if isinstance(v, str) else v
                   for k, v in CAROUSEL_SLIDE_TEMPLATES["cover"].items()},
    })

    # Content slides
    content_points = [
        f"Understanding the fundamentals of {topic.lower()}",
        f"Common mistakes teams make with {topic.lower()}",
        f"Best practices from industry leaders",
        f"Tools and frameworks to consider",
        f"How to measure success",
        f"Getting started: your first steps",
        f"Advanced strategies for scaling",
        f"Real-world examples and case studies",
    ]
    random.shuffle(content_points)

    for i in range(min(num_slides - 2, len(content_points))):
        slides.append({
            "slide_number": i + 2,
            "type": "content",
            "heading": content_points[i],
            "body": f"Brief explanation with 2-3 key bullet points about {content_points[i].lower()}.",
            "design": {k: v.format(**BRAND["colors"]) if isinstance(v, str) else v
                       for k, v in CAROUSEL_SLIDE_TEMPLATES["content"].items()},
        })

    # Closing slide
    slides.append({
        "slide_number": len(slides) + 1,
        "type": "closing",
        "heading": "Follow @elianatech for more",
        "body": "Save this post • Share with your team • Visit elianatech.com",
        "design": {k: v.format(**BRAND["colors"]) if isinstance(v, str) else v
                   for k, v in CAROUSEL_SLIDE_TEMPLATES["closing"].items()},
    })

    # Generate caption
    slide_summary = "\n".join([f"  📌 Slide {s['slide_number']}: {s['heading']}" for s in slides[1:-1]])
    caption_template = random.choice(CAPTION_TEMPLATES["carousel"])
    caption = caption_template.format(
        topic=topic,
        hashtags=hashtags,
        slide_summary=slide_summary,
        slide_count=str(len(slides)),
    )

    return {
        "type": "carousel",
        "topic": topic,
        "slide_count": len(slides),
        "slides": slides,
        "caption": caption,
        "brand_colors": BRAND["colors"],
        "fonts": BRAND["fonts"],
        "dimensions": "1080x1080px per slide",
    }


def generate_story_series(topic: str) -> dict:
    """Generate an Instagram story series concept."""
    category = detect_category(topic)

    stories = [
        {
            "story_number": 1,
            "type": "hook",
            "content": f"Did you know this about {topic}? 🤔",
            "design": "Full-screen gradient background with large text",
            "interactive": "Poll sticker: 'Yes / Tell me more'",
        },
        {
            "story_number": 2,
            "type": "fact",
            "content": f"Here's a surprising fact about {topic.lower()} that most people don't know...",
            "design": "Dark background with highlighted stat number",
            "interactive": None,
        },
        {
            "story_number": 3,
            "type": "tip",
            "content": f"Our top tip for {topic.lower()}: Start small, measure everything, iterate fast.",
            "design": "Brand colors with icon illustration",
            "interactive": "Quiz sticker: test your knowledge",
        },
        {
            "story_number": 4,
            "type": "engagement",
            "content": f"What's your biggest challenge with {topic.lower()}?",
            "design": "Simple text on gradient",
            "interactive": "Question sticker for audience responses",
        },
        {
            "story_number": 5,
            "type": "cta",
            "content": "Want to learn more? Check out our latest blog post.",
            "design": "Brand card with link preview",
            "interactive": "Link sticker to elianatech.com/blog",
        },
    ]

    return {
        "type": "story_series",
        "topic": topic,
        "story_count": len(stories),
        "stories": stories,
        "best_posting_time": "9-11 AM or 7-9 PM (audience timezone)",
        "notes": "Post all stories within 1-2 hours for maximum retention",
    }


def generate_reel_concept(topic: str) -> dict:
    """Generate an Instagram Reel concept/script."""
    return {
        "type": "reel_concept",
        "topic": topic,
        "duration": "30-60 seconds",
        "script": {
            "hook": f"Stop scrolling if you work with {topic.lower()}. (0-3 sec)",
            "problem": f"Most teams get {topic.lower()} wrong because they start with the tool, not the problem. (3-10 sec)",
            "solution": f"Here are 3 things you should do instead... (10-15 sec)",
            "point_1": "First: Define your success metrics BEFORE choosing technology. (15-25 sec)",
            "point_2": "Second: Start with a pilot project, not a full rollout. (25-35 sec)",
            "point_3": "Third: Invest in training. Tools are only as good as the people using them. (35-45 sec)",
            "cta": "Follow @elianatech for more practical tech tips. Link in bio. (45-60 sec)",
        },
        "visual_notes": [
            "Face-to-camera or screen recording with voiceover",
            "Use text overlays for key points",
            "Brand-colored text animations",
            "Background music: upbeat, tech/electronic (royalty-free)",
        ],
        "hashtags": "#TechTips #ElianaTech #Reels #TechReels #LearnOnInstagram",
    }


# ──────────────────────────────────────────────────────────────
# Output Formatting
# ──────────────────────────────────────────────────────────────

def print_single_post(post: dict):
    """Pretty-print a single post."""
    print(f"\n{'═' * 60}")
    print(f"  INSTAGRAM SINGLE POST — {post['topic']}")
    print(f"{'═' * 60}")

    print(f"\n📝 CAPTION:\n")
    print(post["caption"])

    print(f"\n🎨 DESIGN BRIEF:")
    for key, value in post["design_brief"].items():
        if isinstance(value, list):
            print(f"  {key}: {', '.join(value)}")
        else:
            print(f"  {key}: {value}")

    print(f"\n🎨 BRAND COLORS:")
    for name, color in post["brand_colors"].items():
        print(f"  {name}: {color}")

    print(f"\n📐 STYLE NOTES:")
    for note in post["style_notes"]:
        print(f"  • {note}")


def print_carousel(carousel: dict):
    """Pretty-print a carousel."""
    print(f"\n{'═' * 60}")
    print(f"  INSTAGRAM CAROUSEL — {carousel['topic']}")
    print(f"  {carousel['slide_count']} slides | {carousel['dimensions']}")
    print(f"{'═' * 60}")

    print(f"\n📝 CAPTION:\n")
    print(carousel["caption"])

    print(f"\n📑 SLIDES:\n")
    for slide in carousel["slides"]:
        print(f"  ┌─ Slide {slide['slide_number']} ({slide['type'].upper()}) ──────────")
        print(f"  │ Heading: {slide['heading']}")
        if "body" in slide:
            print(f"  │ Body: {slide['body']}")
        if "subheading" in slide:
            print(f"  │ Subheading: {slide['subheading']}")
        print(f"  │ Design: {slide['design']['background']}")
        print(f"  └──────────────────────────────────")

    print(f"\n🎨 FONTS:")
    for name, font in carousel["fonts"].items():
        print(f"  {name}: {font}")


def print_story_series(stories: dict):
    """Pretty-print a story series."""
    print(f"\n{'═' * 60}")
    print(f"  INSTAGRAM STORY SERIES — {stories['topic']}")
    print(f"  {stories['story_count']} stories")
    print(f"{'═' * 60}")

    for story in stories["stories"]:
        print(f"\n  ┌─ Story {story['story_number']} ({story['type'].upper()}) ──────────")
        print(f"  │ Content: {story['content']}")
        print(f"  │ Design: {story['design']}")
        if story.get("interactive"):
            print(f"  │ Interactive: {story['interactive']}")
        print(f"  └──────────────────────────────────")

    print(f"\n⏰ Best posting time: {stories['best_posting_time']}")
    print(f"📌 {stories['notes']}")


def print_reel_concept(reel: dict):
    """Pretty-print a reel concept."""
    print(f"\n{'═' * 60}")
    print(f"  INSTAGRAM REEL CONCEPT — {reel['topic']}")
    print(f"  Duration: {reel['duration']}")
    print(f"{'═' * 60}")

    print(f"\n🎬 SCRIPT:\n")
    for section, text in reel["script"].items():
        print(f"  [{section.upper()}]")
        print(f"  {text}\n")

    print(f"🎥 VISUAL NOTES:")
    for note in reel["visual_notes"]:
        print(f"  • {note}")

    print(f"\n# {reel['hashtags']}")


# ──────────────────────────────────────────────────────────────
# Interactive Mode
# ──────────────────────────────────────────────────────────────

def interactive_mode():
    """Run the generator interactively."""
    print("=" * 60)
    print("  ElianaTech Instagram Content Generator")
    print("=" * 60)
    print()

    topic = input("Enter topic (e.g., Cloud Computing, AI Strategy): ").strip()
    if not topic:
        topic = "Digital Transformation"

    print()
    print("Available formats:")
    print("  1. single    — Single image post with caption + design brief")
    print("  2. carousel  — Multi-slide carousel (5-10 slides)")
    print("  3. story     — Story series (5 stories)")
    print("  4. reel      — Reel concept and script")
    print("  5. all       — Generate all formats")
    print()

    format_choice = input("Choose format [1-5, default=1]: ").strip()
    format_map = {"1": "single", "2": "carousel", "3": "story", "4": "reel", "5": "all"}
    post_format = format_map.get(format_choice, "single")

    if post_format in ("single", "all"):
        post = generate_single_post(topic)
        print_single_post(post)

    if post_format in ("carousel", "all"):
        num_slides = 7
        if post_format != "all":
            slides_input = input("\nNumber of slides [5-10, default=7]: ").strip()
            try:
                num_slides = min(10, max(5, int(slides_input)))
            except ValueError:
                num_slides = 7
        carousel = generate_carousel(topic, num_slides)
        print_carousel(carousel)

    if post_format in ("story", "all"):
        stories = generate_story_series(topic)
        print_story_series(stories)

    if post_format in ("reel", "all"):
        reel = generate_reel_concept(topic)
        print_reel_concept(reel)

    print(f"\n{'=' * 60}")
    print("  Customize the content above to match your brand voice!")
    print(f"{'=' * 60}")

    # Offer to export
    export = input("\nExport to JSON? [y/N]: ").strip().lower()
    if export == "y":
        data = {"topic": topic, "generated_at": datetime.now().isoformat()}
        if post_format in ("single", "all"):
            data["single_post"] = generate_single_post(topic)
        if post_format in ("carousel", "all"):
            data["carousel"] = generate_carousel(topic)
        if post_format in ("story", "all"):
            data["story_series"] = generate_story_series(topic)
        if post_format in ("reel", "all"):
            data["reel_concept"] = generate_reel_concept(topic)

        filename = f"ig-content-{topic.lower().replace(' ', '-')}-{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n✅ Exported to {filename}")


def suggest_content_calendar(weeks: int = 4) -> list:
    """Generate a suggested IG content calendar."""
    all_ideas = []
    for category, ideas in TOPIC_IDEAS.items():
        for idea in ideas:
            idea["category"] = category
            all_ideas.append(idea)

    random.shuffle(all_ideas)
    calendar = []
    days = ["Mon", "Wed", "Fri"]  # 3 posts per week

    for week in range(1, weeks + 1):
        for day_idx, day in enumerate(days):
            if all_ideas:
                idea = all_ideas.pop(0)
                calendar.append({
                    "week": week,
                    "day": day,
                    "title": idea["title"],
                    "format": idea["type"],
                    "category": idea["category"],
                })

    return calendar


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="ElianaTech Instagram Photo Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              %(prog)s --topic "Cloud Computing"
              %(prog)s --topic "AI Trends" --format carousel --slides 8
              %(prog)s --topic "Cybersecurity" --format story
              %(prog)s --topic "DevOps" --format reel
              %(prog)s --calendar 4
              %(prog)s --interactive
        """),
    )
    parser.add_argument("--topic", type=str, help="The topic for the content")
    parser.add_argument("--format", type=str, default="single",
                        choices=["single", "carousel", "story", "reel", "all"],
                        help="Content format (default: single)")
    parser.add_argument("--slides", type=int, default=7, help="Number of carousel slides (5-10)")
    parser.add_argument("--calendar", type=int, metavar="WEEKS",
                        help="Generate a content calendar for N weeks")
    parser.add_argument("--export-json", action="store_true", help="Export output as JSON")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if args.calendar:
        calendar = suggest_content_calendar(args.calendar)
        print(f"\n{'═' * 60}")
        print(f"  INSTAGRAM CONTENT CALENDAR — {args.calendar} Weeks")
        print(f"{'═' * 60}\n")
        current_week = 0
        for entry in calendar:
            if entry["week"] != current_week:
                current_week = entry["week"]
                print(f"\n  Week {current_week}:")
            print(f"    {entry['day']} | [{entry['format'].upper():10s}] {entry['title']} ({entry['category']})")
        return

    if not args.topic:
        parser.print_help()
        print("\nError: --topic is required (or use --interactive / --calendar)")
        return

    results = {}

    if args.format in ("single", "all"):
        post = generate_single_post(args.topic)
        print_single_post(post)
        results["single_post"] = post

    if args.format in ("carousel", "all"):
        slides = min(10, max(5, args.slides))
        carousel = generate_carousel(args.topic, slides)
        print_carousel(carousel)
        results["carousel"] = carousel

    if args.format in ("story", "all"):
        stories = generate_story_series(args.topic)
        print_story_series(stories)
        results["story_series"] = stories

    if args.format in ("reel", "all"):
        reel = generate_reel_concept(args.topic)
        print_reel_concept(reel)
        results["reel_concept"] = reel

    if args.export_json and results:
        results["topic"] = args.topic
        results["generated_at"] = datetime.now().isoformat()
        filename = f"ig-content-{args.topic.lower().replace(' ', '-')}-{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n✅ Exported to {filename}")


if __name__ == "__main__":
    main()
