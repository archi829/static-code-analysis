## 🧾 Known Issues Table

| Issue | Tool(s) | Type | Line(s) | Description | Fix Approach |
|:------|:---------|:------|:--------|:-------------|:--------------|
| C0114 | Pylint | Module Style | 1 | Missing module docstring. | Add a docstring at the top of the file. |
| W0611 / F401 | Pylint / Flake8 | Unused Import | 2 | Import of logging module is unused. | Remove the unused `import logging` line. |
| C0116 | Pylint | Documentation | 7, 13, 21, 24, 30, 35, 40, 47 | Missing function or method docstring for all functions. | Add docstrings to all function definitions. |
| C0103 | Pylint | Naming | 7, 13, 21, 24, 30, 35, 40, 47 | Function names (e.g., `addItem`) do not conform to snake_case style. | Rename all functions to use snake_case (e.g., `add_item`). |
| W0102 | Pylint | Potential Bug | 7 | Dangerous default value (`[]`) used as an argument. | Change the default value to `None` and initialize the list inside the function. |
| C0209 | Pylint | Style | 11 | Using `%` or `.format()` when an f-string could be used. | Convert the string formatting in `logs.append()` to an f-string. |
| W0702 / E722 / B110 | Pylint / Flake8 / Bandit | Error / Security | 18 | Bare `except` statement used, catching all exceptions and hiding bugs. | Specify the exception type to catch (e.g., `except KeyError:`). |
| R1732 / W1514 | Pylint | Resource Mgmt / I/O | 25, 31 | `open()` calls are not wrapped in a `with` statement and lack encoding. | Use `with open(..., encoding='utf-8') as f:` to manage resources and encoding. |
| W0603 | Pylint | Code Smell | 26 | Using the `global` statement to modify a module-level variable. | Refactor the code to avoid `global` (e.g., use a class or return the data). |
| W0123 / B307 | Pylint / Bandit | Security | 58 | Use of the potentially insecure function `eval()`. | Remove the call to `eval()` or use `ast.literal_eval` for safe literal parsing. |
| E302 / E305 | Flake8 | Whitespace | Various | Incorrect blank lines before/after function definitions. | Add or adjust blank lines to ensure 2 lines before and after function definitions. |
