# nicegui

**nicegui** lets you build **web user interfaces entirely in Python**. You
write Python code with a friendly `ui.*` API (buttons, sliders, inputs,
plots, tables…) and NiceGUI turns it into a responsive web page served over
HTTP/WebSocket — no HTML/CSS/JavaScript required (though you can add them).

## Why use it?

- The front end lives in the same file/language as your backend logic.
- Two-way binding: UI events call your Python functions, and your Python can
  update the UI live (e.g. via `ui.timer`).
- Fast to prototype tools, dashboards, and admin panels.
- Rich element library: plots, charts, data tables, uploads, images, 3D scenes.

## Key features

- `ui.label`, `ui.button`, `ui.input`, `ui.slider`, `ui.select`, `ui.toggle`…
- Event handlers (`on_click`, `on_change`) wired to plain Python callables.
- `@ui.page('/path')` for multi-page apps.
- `ui.timer` for periodic background updates pushed to the browser.
- `ui.notify`, `ui.markdown`, `ui.plot` (Plotly), `ui.table`, `ui.upload`.
- `ui.run(...)` — serves the app locally; options for port, auto-reload, etc.
- Styling via Tailwind-like `.classes(...)` and `.style(...)` helpers.

## Install

```bash
pip install nicegui
```

## Use cases

- Internal tools, dashboards, and admin consoles.
- Prototyping a GUI for a Python script/algorithm.
- Live data visualizations and monitoring screens.
- Quickly exposing a Python API through a clickable web page.

## Things you can achieve

- A counter button that updates a label when clicked.
- A slider that live-updates a computed value.
- A background `ui.timer` that refreshes data every second.
- A multi-element form that reacts to input in real time.

## References

- Docs: https://nicegui.io/documentation
- PyPI: https://pypi.org/project/nicegui/
- GitHub: https://github.com/zauberzeug/nicegui
