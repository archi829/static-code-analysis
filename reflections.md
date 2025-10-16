# 🪞 Reflection
---

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

- The easiest issues to fix were **unused imports** and **missing blank lines**, since they only required simple deletions or formatting adjustments.  
- The hardest issues involved **function renaming (C0103)** and **adding proper docstrings (C0116)** because they required ensuring consistency across multiple functions and describing their logic clearly.

---

### 2. Did the static analysis tools report any false positives?

- Yes, there was a **false positive** with the global `stock_data` warning (**W0602**).  
- After refactoring `load_data` to use `stock_data.update()`, the global keyword became unnecessary.  
- The tool correctly flagged it as dead code—even though it was initially intentional—showing that static analysis can sometimes over-warn before contextual fixes are made.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?

- I would enforce quality checks at two levels:
  - **Locally:** Use **pre-commit hooks** to automatically run Flake8 before every commit.
  - **Remotely:** Set up a **CI/CD pipeline** to run comprehensive **Bandit** and **Pylint** scans on every pull request.  
- This ensures that critical issues block merges, maintaining consistent code quality and security across the project.

---

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Robustness:** Improved by replacing bare `except` statements with specific exception handling and using `with open(...)` to manage file resources safely.  
- **Readability:** Greatly enhanced after renaming all functions to **snake_case** and adding **docstrings**, making the code cleaner, more Pythonic, and easier for others to understand.  
- Overall, the codebase became more maintainable and aligned with standard Python best practices.

---
