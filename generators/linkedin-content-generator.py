#!/usr/bin/env python3
"""
ElianaTech LinkedIn Content Generator

Generates LinkedIn posts from blog articles, topics, or custom inputs.
Supports multiple post formats: thought leadership, how-to, listicle,
story, and promotional.

Usage:
    python linkedin-content-generator.py --topic "Cloud Migration"
    python linkedin-content-generator.py --topic "AI Trends" --format thought-leadership
    python linkedin-content-generator.py --blog-title "How to Deploy K8s" --blog-url "https://elianatech.com/blog/..."
    python linkedin-content-generator.py --interactive
"""

import argparse
import random
import textwrap
from datetime import datetime


# --- Post Templates ---

TEMPLATES = {
    "thought-leadership": [
        textwrap.dedent("""\
            Most companies get {topic} wrong.

            Here's what I've seen after working with dozens of teams:

            {point_1}
            {point_2}
            {point_3}

            The real question isn't whether to invest in {topic}.
            It's whether you can afford not to.

            {cta}

            #ElianaTech #Technology #{hashtag}"""),
        textwrap.dedent("""\
            Unpopular opinion about {topic}:

            {hook}

            Here's why this matters:

            → {point_1}
            → {point_2}
            → {point_3}

            The companies winning right now understand this.
            The rest are playing catch-up.

            {cta}

            #ElianaTech #{hashtag} #TechLeadership"""),
        textwrap.dedent("""\
            I've been thinking a lot about {topic} lately.

            And one thing keeps coming up:

            {hook}

            Here are 3 things every leader should consider:

            1️⃣ {point_1}
            2️⃣ {point_2}
            3️⃣ {point_3}

            What's your take? Drop your thoughts below 👇

            #ElianaTech #{hashtag} #Innovation"""),
    ],
    "how-to": [
        textwrap.dedent("""\
            Want to get started with {topic}?

            Here's a simple framework we use at ElianaTech:

            Step 1: {step_1}
            Step 2: {step_2}
            Step 3: {step_3}
            Step 4: {step_4}
            Step 5: {step_5}

            The key? Start small, iterate fast, measure everything.

            {cta}

            #ElianaTech #{hashtag} #HowTo"""),
        textwrap.dedent("""\
            Stop overcomplicating {topic}.

            Here's the straightforward approach that actually works:

            ✅ {step_1}
            ✅ {step_2}
            ✅ {step_3}
            ✅ {step_4}

            We've helped teams implement this in weeks, not months.

            {cta}

            #ElianaTech #{hashtag} #TechTips"""),
    ],
    "listicle": [
        textwrap.dedent("""\
            {number} things I wish someone told me about {topic}:

            1. {item_1}
            2. {item_2}
            3. {item_3}
            4. {item_4}
            5. {item_5}

            Which one resonates most with you?

            {cta}

            #ElianaTech #{hashtag} #LessonsLearned"""),
        textwrap.dedent("""\
            {topic} in 2026: {number} trends to watch

            🔹 {item_1}
            🔹 {item_2}
            🔹 {item_3}
            🔹 {item_4}
            🔹 {item_5}

            The landscape is shifting fast.
            Which trend has your attention?

            {cta}

            #ElianaTech #{hashtag} #TechTrends"""),
    ],
    "story": [
        textwrap.dedent("""\
            Last month, a client came to us with a challenge:

            "{problem}"

            They had tried everything. Nothing worked.

            So here's what we did differently:

            {solution}

            The result?

            {result}

            Sometimes the answer isn't more technology.
            It's the right technology, applied the right way.

            {cta}

            #ElianaTech #{hashtag} #ClientSuccess"""),
        textwrap.dedent("""\
            3 years ago, we made a bet on {topic}.

            Everyone said it was too early.
            Everyone said the market wasn't ready.

            Today?

            {outcome}

            The lesson: {lesson}

            {cta}

            #ElianaTech #{hashtag} #Growth"""),
    ],
    "blog-promotion": [
        textwrap.dedent("""\
            New on the ElianaTech blog 📝

            {blog_title}

            {summary}

            Key takeaways:
            → {takeaway_1}
            → {takeaway_2}
            → {takeaway_3}

            Read the full article: {blog_url}

            #ElianaTech #{hashtag} #TechBlog"""),
        textwrap.dedent("""\
            We just published a deep-dive on {topic}.

            "{blog_title}"

            Here's what you'll learn:

            ✅ {takeaway_1}
            ✅ {takeaway_2}
            ✅ {takeaway_3}

            Worth a 5-minute read if you're dealing with {topic}.

            Link in comments 👇

            #ElianaTech #{hashtag}"""),
    ],
}

# --- Hook Library ---

HOOKS = {
    "cloud": [
        "Cloud migration isn't about moving servers. It's about rethinking how you build.",
        "90% of cloud cost overruns come from the same 3 mistakes.",
        "The cloud doesn't save money by default. Strategy saves money.",
    ],
    "ai": [
        "AI won't replace your team. But a team using AI will replace one that doesn't.",
        "The biggest AI risk isn't bias or hallucination. It's deploying without a clear use case.",
        "Most AI projects fail not because of the model, but because of the data.",
    ],
    "security": [
        "The average breach costs $4.5M. But the real cost is trust.",
        "Your security is only as strong as your least-trained employee.",
        "Zero trust isn't paranoia. It's the new baseline.",
    ],
    "development": [
        "The best code is the code you don't write.",
        "Speed to market means nothing if you're shipping tech debt.",
        "Your architecture decisions today become your constraints tomorrow.",
    ],
    "data": [
        "You don't have a data problem. You have a data strategy problem.",
        "Every company is a data company. Most just don't know it yet.",
        "The difference between data and insights? A good question.",
    ],
    "general": [
        "Technology is easy. Transformation is hard.",
        "The best technology investment is the one that solves a real problem.",
        "Digital transformation isn't a project. It's a way of operating.",
    ],
}

# --- CTA Library ---

CTAS = [
    "Want to talk about how this applies to your business? DM me or visit elianatech.com",
    "Follow ElianaTech for more insights on building better technology.",
    "We help companies navigate exactly these challenges. Learn more at elianatech.com",
    "What's been your experience? Share in the comments.",
    "Agree? Disagree? I'd love to hear your perspective.",
    "If this resonated, share it with someone who needs to hear it.",
    "Follow along for more practical tech insights every week.",
    "Book a free consultation at elianatech.com/contact",
]

# --- Hashtag Library ---

HASHTAGS = {
    "cloud": ["CloudComputing", "CloudMigration", "AWS", "Azure", "GCP", "DevOps"],
    "ai": ["ArtificialIntelligence", "MachineLearning", "AI", "GenerativeAI", "MLOps"],
    "security": ["CyberSecurity", "InfoSec", "ZeroTrust", "DataSecurity", "AppSec"],
    "development": ["SoftwareDevelopment", "WebDev", "Programming", "CleanCode", "Agile"],
    "data": ["DataAnalytics", "DataEngineering", "BigData", "DataScience", "DataPipelines"],
    "general": ["DigitalTransformation", "TechStrategy", "Innovation", "StartupTech", "TechLeadership"],
}


def detect_category(topic: str) -> str:
    """Detect the content category from the topic string."""
    topic_lower = topic.lower()
    if any(w in topic_lower for w in ["cloud", "aws", "azure", "gcp", "infrastructure", "kubernetes", "k8s"]):
        return "cloud"
    if any(w in topic_lower for w in ["ai", "machine learning", "ml", "llm", "gpt", "neural", "deep learning"]):
        return "ai"
    if any(w in topic_lower for w in ["security", "cyber", "breach", "zero trust", "soc", "compliance"]):
        return "security"
    if any(w in topic_lower for w in ["software", "code", "develop", "api", "frontend", "backend", "fullstack"]):
        return "development"
    if any(w in topic_lower for w in ["data", "analytics", "pipeline", "database", "sql", "warehouse"]):
        return "data"
    return "general"


def generate_post(topic: str, post_format: str = "thought-leadership",
                  blog_title: str = "", blog_url: str = "") -> str:
    """Generate a LinkedIn post based on topic and format."""
    category = detect_category(topic)
    hook = random.choice(HOOKS.get(category, HOOKS["general"]))
    cta = random.choice(CTAS)
    hashtag = random.choice(HASHTAGS.get(category, HASHTAGS["general"]))

    templates = TEMPLATES.get(post_format, TEMPLATES["thought-leadership"])
    template = random.choice(templates)

    placeholders = {
        "topic": topic,
        "hook": hook,
        "cta": cta,
        "hashtag": hashtag,
        "blog_title": blog_title or f"Deep Dive: {topic}",
        "blog_url": blog_url or "https://elianatech.com/blog",
        "number": str(random.choice([5, 7, 10])),
        "problem": f"We can't scale our {topic.lower()} fast enough.",
        "solution": f"We implemented a phased approach to {topic.lower()}, focusing on quick wins first.",
        "result": f"3x improvement in efficiency. 40% cost reduction. Zero downtime.",
        "outcome": f"{topic} is now one of the most in-demand capabilities in the industry.",
        "lesson": "Bet on where the industry is going, not where it is.",
        "summary": f"A comprehensive look at {topic.lower()} — what works, what doesn't, and what's next.",
    }

    # Generate numbered/bulleted placeholders
    point_stubs = [
        f"Start with strategy, not technology",
        f"Measure outcomes, not outputs",
        f"Invest in your team's skills, not just tools",
        f"Build for iteration, not perfection",
        f"Focus on the problem, not the solution",
    ]
    random.shuffle(point_stubs)

    step_stubs = [
        f"Assess your current state honestly",
        f"Define clear success metrics",
        f"Start with a proof of concept",
        f"Build internal champions",
        f"Scale what works, kill what doesn't",
    ]

    item_stubs = [
        f"AI-augmented development is becoming the norm",
        f"Platform engineering is replacing pure DevOps",
        f"Edge computing is gaining real enterprise traction",
        f"Data mesh architecture is maturing",
        f"Security is shifting further left in the pipeline",
    ]

    takeaway_stubs = [
        f"Why most teams struggle with {topic.lower()}",
        f"The #1 mistake to avoid when implementing {topic.lower()}",
        f"A practical framework you can apply this week",
    ]

    for i, stub in enumerate(point_stubs[:5], 1):
        placeholders[f"point_{i}"] = stub
    for i, stub in enumerate(step_stubs[:5], 1):
        placeholders[f"step_{i}"] = stub
    for i, stub in enumerate(item_stubs[:5], 1):
        placeholders[f"item_{i}"] = stub
    for i, stub in enumerate(takeaway_stubs[:3], 1):
        placeholders[f"takeaway_{i}"] = stub

    try:
        return template.format(**placeholders)
    except KeyError as e:
        return f"[Template error: missing placeholder {e}]\n\n{template}"


def interactive_mode():
    """Run the generator in interactive mode."""
    print("=" * 60)
    print("  ElianaTech LinkedIn Content Generator")
    print("=" * 60)
    print()

    topic = input("Enter topic (e.g., Cloud Migration, AI Strategy): ").strip()
    if not topic:
        topic = "Digital Transformation"

    print()
    print("Available formats:")
    print("  1. thought-leadership  (opinion / insight posts)")
    print("  2. how-to              (step-by-step guides)")
    print("  3. listicle            (numbered list posts)")
    print("  4. story               (narrative / case study posts)")
    print("  5. blog-promotion      (promote a blog article)")
    print()

    format_choice = input("Choose format [1-5, default=1]: ").strip()
    format_map = {
        "1": "thought-leadership",
        "2": "how-to",
        "3": "listicle",
        "4": "story",
        "5": "blog-promotion",
    }
    post_format = format_map.get(format_choice, "thought-leadership")

    blog_title = ""
    blog_url = ""
    if post_format == "blog-promotion":
        blog_title = input("Blog article title: ").strip()
        blog_url = input("Blog article URL: ").strip()

    num_variations = input("How many variations? [1-5, default=3]: ").strip()
    try:
        num_variations = min(5, max(1, int(num_variations)))
    except ValueError:
        num_variations = 3

    print()
    print("=" * 60)
    print(f"  Generated {num_variations} LinkedIn post(s) for: {topic}")
    print("=" * 60)

    for i in range(num_variations):
        print(f"\n{'─' * 60}")
        print(f"  VARIATION {i + 1}")
        print(f"{'─' * 60}\n")
        post = generate_post(topic, post_format, blog_title, blog_url)
        print(post)

    print(f"\n{'=' * 60}")
    print("  Copy your favorite and customize before posting!")
    print(f"{'=' * 60}")


def batch_generate(topics: list, post_format: str = "thought-leadership",
                   variations: int = 1) -> list:
    """Generate posts for multiple topics at once."""
    results = []
    for topic in topics:
        for _ in range(variations):
            post = generate_post(topic, post_format)
            results.append({"topic": topic, "format": post_format, "post": post})
    return results


def main():
    parser = argparse.ArgumentParser(
        description="ElianaTech LinkedIn Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              %(prog)s --topic "Cloud Migration"
              %(prog)s --topic "AI Strategy" --format thought-leadership
              %(prog)s --topic "Kubernetes" --format how-to --variations 3
              %(prog)s --blog-title "My Article" --blog-url "https://..."
              %(prog)s --interactive
        """),
    )
    parser.add_argument("--topic", type=str, help="The topic for the post")
    parser.add_argument("--format", type=str, default="thought-leadership",
                        choices=["thought-leadership", "how-to", "listicle", "story", "blog-promotion"],
                        help="Post format (default: thought-leadership)")
    parser.add_argument("--blog-title", type=str, default="", help="Blog article title (for blog-promotion format)")
    parser.add_argument("--blog-url", type=str, default="", help="Blog article URL (for blog-promotion format)")
    parser.add_argument("--variations", type=int, default=3, help="Number of post variations to generate (1-5)")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.topic:
        parser.print_help()
        print("\nError: --topic is required (or use --interactive mode)")
        return

    variations = min(5, max(1, args.variations))

    print(f"\nGenerating {variations} LinkedIn post(s) for: {args.topic}\n")
    print(f"Format: {args.format}")
    print("=" * 60)

    for i in range(variations):
        print(f"\n{'─' * 60}")
        print(f"  VARIATION {i + 1}")
        print(f"{'─' * 60}\n")
        post = generate_post(args.topic, args.format, args.blog_title, args.blog_url)
        print(post)

    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
