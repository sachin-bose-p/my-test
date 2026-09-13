# AI CODING AGENT DIRECTIVES & CONTEXT SPECIFICATION
## Repository: My Test

> High-density, token-optimized context specification for AI coding agents.
> Agents MUST load and abide by these rules before executing any code modifications.

---

### 1. Hard Agent Directives (MANDATORY)
1. **Surgical Precision**: Output ONLY the exact lines or functions needing edits. NEVER rewrite whole files unnecessarily.
2. **Zero Hallucinated Dependencies**: Do NOT import packages, CDNs, or libraries that are not already present in the manifests below.
3. **Preserve Public Contracts**: Do NOT modify existing function signatures, component props, or database schemas without explicit instruction.
4. **Theme Token Fidelity**: ALWAYS use the project's native CSS variables. Do NOT invent new color codes.
5. **Static Verification**: Run static syntax checks or linters before presenting changes.

---

### 2. Active Design System Tokens
| Token Name | Defined Value / Description |
| :--- | :--- |
| `--bg-color` | `#0f172a` |
| `--card-bg` | `#1e293b` |
| `--text-primary` | `#f8fafc` |
| `--text-secondary` | `#94a3b8` |
| `--accent-color` | `#38bdf8` |
| `--accent-hover` | `#0ea5e9` |
| `--border-color` | `#334155` |
- **Typography**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`
- **UI Architecture**: CSS3 Custom Properties (:root theme)

---

### 3. Detected Technology Stack
- **Frameworks**: HTML5 / Modern CSS3 / Vanilla JS
- **State Model**: DOM Events, Vanilla JS Local State
- **Package Ecosystem**: None (Static Web / CDN)

---

### 4. Behavioral Guardrails
- **DO**:
  - Match code style: 2 spaces, double quotes.
  - Check element existence with `document.querySelector` before binding events.
  - Retain comments and documentation headers.
- **DO NOT**:
  - Introduce new CSS frameworks (e.g. do not inject Tailwind if project is Vanilla CSS).
  - Delete or reformat unrelated code blocks.
  - Leave console debug statements or scratch logs in production files.
