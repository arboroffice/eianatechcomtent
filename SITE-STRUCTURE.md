# ElianaTech.com — Site Structure & Information Architecture

> **Version:** 1.0
> **Date:** 2026-02-26

---

## Navigation Structure

### Primary Navigation

```
Home | Services ▾ | Blog | Case Studies | About | Contact
```

### Services Dropdown

```
Services
├── Software Development
├── Cloud & Infrastructure
├── Data & Analytics
├── AI & Machine Learning
├── Cybersecurity
└── IT Consulting
```

### Footer Navigation

```
Footer
├── Services
│   ├── Software Development
│   ├── Cloud & Infrastructure
│   ├── Data & Analytics
│   ├── AI & Machine Learning
│   ├── Cybersecurity
│   └── IT Consulting
├── Company
│   ├── About Us
│   ├── Careers
│   ├── Partners
│   └── Contact
├── Resources
│   ├── Blog
│   ├── Case Studies
│   ├── Whitepapers
│   └── Newsletter
└── Legal
    ├── Privacy Policy
    ├── Terms of Service
    └── Cookie Policy
```

---

## Full Sitemap

```
elianatech.com/
│
├── index                           Homepage
│
├── about/                          About ElianaTech
│   ├── team                        Meet the team
│   └── careers                     Open positions
│
├── services/                       Services overview
│   ├── software-development        Custom software development
│   ├── cloud-infrastructure        Cloud & infrastructure services
│   ├── data-analytics              Data & analytics solutions
│   ├── ai-machine-learning         AI & ML services
│   ├── cybersecurity               Cybersecurity services
│   └── it-consulting               IT consulting & strategy
│
├── blog/                           Blog listing (paginated)
│   ├── category/[category]         Blog category pages
│   ├── tag/[tag]                   Blog tag pages
│   └── [slug]                      Individual blog posts
│
├── case-studies/                   Case studies listing
│   └── [slug]                      Individual case studies
│
├── resources/                      Resource center
│   ├── whitepapers                 Downloadable whitepapers
│   ├── guides                      Technical guides
│   └── tools                       Free tools & calculators
│
├── contact                         Contact page
├── newsletter                      Newsletter signup
├── privacy-policy                  Privacy policy
├── terms-of-service                Terms of service
├── cookie-policy                   Cookie policy
├── sitemap.xml                     XML sitemap
└── robots.txt                      Robots file
```

---

## Page Hierarchy & URL Structure

### URL Conventions
- All lowercase
- Hyphens for word separation (no underscores)
- No trailing slashes
- Maximum 3 levels deep
- Descriptive and keyword-rich

### Examples
```
✅ /services/software-development
✅ /blog/how-to-deploy-kubernetes-cluster
✅ /case-studies/fintech-startup-cloud-migration

❌ /services/Software_Development
❌ /blog/post?id=123
❌ /services/dev/custom/enterprise/solutions
```

---

## Page Templates

### Template 1: Landing Page
Used for: Homepage, service pages
- Hero section with CTA
- Feature/benefit blocks
- Social proof section
- Content section
- CTA banner

### Template 2: Content Page
Used for: About, careers, individual services
- Page header (title + subtitle)
- Rich text content area
- Sidebar (optional)
- Related content section
- CTA section

### Template 3: Blog Post
Used for: Individual blog articles
- Article header (title, date, author, category, reading time)
- Featured image
- Article body (rich text)
- Author bio box
- Related articles (3)
- Comments section (optional)
- Social share buttons

### Template 4: Case Study
Used for: Individual case studies
- Header (client name, industry, service used)
- Challenge section
- Solution section
- Results section (with metrics)
- Testimonial quote block
- Related case studies

### Template 5: Listing Page
Used for: Blog index, case studies index, resource center
- Page header with description
- Filter/category bar
- Content grid or list
- Pagination
- Sidebar with popular/featured content

---

## Technical Notes

### Responsive Breakpoints
- Mobile: 0–767px
- Tablet: 768–1023px
- Desktop: 1024px+

### Performance Targets
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1
- Time to Interactive: < 3.5s

### Accessibility Requirements
- WCAG 2.1 AA compliance minimum
- Semantic HTML structure
- Keyboard navigable
- Screen reader compatible
- Color contrast ratio ≥ 4.5:1 for normal text
