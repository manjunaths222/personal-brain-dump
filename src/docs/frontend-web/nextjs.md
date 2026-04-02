---
title: "Nextjs"
---

NextJs

What is Next.js: React framework with SSR, routing, and performance optimizations.
Install: npx create-next-app@latest my-app

Core Features: File-based routing, SSR, SSG, API routes, Image optimization, Middleware, App Directory (v13+), TypeScript, Tailwind

Rendering Methods:
- Static Generation (SSG): getStaticProps, getStaticPaths
- Server-Side Rendering (SSR): getServerSideProps
- Client-Side Rendering (CSR): useEffect or SWR
- Incremental Static Regeneration (ISR): revalidate: 10 in getStaticProps

Routing:
- /pages/index.js → /, /pages/about.js → /about
- Dynamic: /pages/blog/[slug].js
- Catch-all: [...slug].js, Optional: [[...slug]].js

API Routes: /pages/api/hello.js → export default function handler(req, res) {}

App Directory (Next.js 13+):
- /app/layout.js, /app/page.js, /app/loading.js, /app/error.js
- Server Components vs Client Components ('use client' directive)

Styling: Global CSS (only in _app.js), CSS Modules, Tailwind, Styled Components/Emotion

Middleware (middleware.js):
```javascript
import { NextResponse } from 'next/server';
export function middleware(req) {
  if (!req.cookies.get('token')) {
    return NextResponse.redirect(new URL('/login', req.url));
  }
  return NextResponse.next();
}
```

Image Optimization: next/image — lazy loading, responsive, WebP

Auth: NextAuth.js, JWT-based Auth with Middleware, Session management

Performance: Code splitting, Lazy loading, Image Optimization, Memoization, ISR, SWR/React Query

SEO: next/head for meta tags, Structured Data, Canonical URLs

Testing: Jest + React Testing Library, Cypress/Playwright, MSW

Deployment: Vercel (official), Netlify, AWS, Docker, Firebase

SSR vs CSR vs SSG:
- SSG: built at compile time, very fast, good for mostly static content
- SSR: built at request time, always fresh, higher server cost
- CSR: rendered in browser, slower initial load, dynamic

System Design with Next.js:
- SSR cache strategies (Redis), CDN (Vercel/Cloudflare)
- Micro-frontends with Module Federation
- API rate limiting in Next.js routes

Project Ideas:
- SaaS Dashboard (Auth + Payments), Personal Blog (Markdown, ISR)
- E-commerce Storefront, Admin Panel, Portfolio Website
