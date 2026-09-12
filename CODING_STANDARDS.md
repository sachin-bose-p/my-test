# CODING STANDARDS & ENGINEERING GUIDELINES
## My Test

> Autonomous engineering standards derived from project manifests, linters, and repository structure.

---

### 1. Code Formatting & Syntax Rules
- **Indentation**: 2 spaces (No mixed tabs and spaces).
- **Quote Style**: Double quotes (\"...\") for HTML attributes & markup.
- **Character Encoding**: UTF-8.
- **Line Endings**: LF (Unix style).

---

### 2. Technology & Language Standards
- **Core Framework**: HTML5 / Modern CSS3 / Vanilla JS
- **Package Manager**: None (Static Web / CDN)

---

### 3. Styling & Design Token Conventions
- **Styling Strategy**: CSS3 Custom Properties (:root theme)
- **Typography / Primary Font**: `system-ui`

#### Theme Tokens:
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
2. **Defensive DOM Operations**: Always verify that DOM nodes exist before attaching event listeners.
3. **Safe State Mutations**: Avoid global variable pollution.
4. **Clean Error Handling**: Wrap network requests in try/catch blocks.
5. **Security First**: Never inject unsanitized user input with .innerHTML.
