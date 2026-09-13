# CODING STANDARDS & ENGINEERING GUIDELINES
## My Test

> Autonomous engineering standards derived from project manifests, linters, and repository structure.

---

### 1. Code Formatting & Syntax Rules
- **Indentation**: 2 spaces (No mixed tabs and spaces).
- **Quote Style**: Double quotes ("...") for HTML attributes & markup.
- **Character Encoding**: UTF-8.
- **Line Endings**: LF (Unix style).
- **Max Line Length**: 100 characters for logic; soft wrap for long template strings.

---

### 2. Technology & Language Standards
- **Core Framework**: HTML5 / Modern CSS3 / Vanilla JS
- **Package Manager**: None (Static Web / CDN)


- **Markup Standards**: Semantic HTML5 tags (<header>, <nav>, <aside>, <main>, <footer>)

---

### 3. Styling & Design Token Conventions
- **Styling Strategy**: CSS3 Custom Properties (:root theme)
- **Typography / Primary Font**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`

- **Design Tokens Enforcement**:
  - NEVER hardcode arbitrary hex colors or pixel sizes when a matching design token exists.
  - Always consume root theme tokens:
    - `--bg-color: #0f172a`
    - `--card-bg: #1e293b`
    - `--text-primary: #f8fafc`
    - `--text-secondary: #94a3b8`
    - `--accent-color: #38bdf8`
    - `--accent-hover: #0ea5e9`
    - `--border-color: #334155`

---

### 4. Code Quality & Modularity Principles
1. **Single Responsibility**: Each function or module must handle exactly one domain task.
2. **Defensive DOM Operations**: Always verify that DOM nodes exist before attaching event listeners or reading attributes.
3. **Safe State Mutations**: Avoid global variable pollution. Encapsulate state within closures, modules, or explicit state stores.
4. **Clean Error Handling**: Wrap network requests and parsing operations in `try/catch` blocks with user-friendly fallbacks.
5. **Security First**: Never inject unsanitized user input with `.innerHTML`. Use `.textContent` or sanitized templates.

---

### 5. Pre-Commit Checklist for Developers & AI Agents
- [ ] No regression in existing functionality or UI layout.
- [ ] CSS modifications utilize official design variables.
- [ ] Code is formatted to 2 spaces.
- [ ] Zero unhandled console errors or runtime warnings.
- [ ] Minimal surgical changes committed without unnecessary file churn.
