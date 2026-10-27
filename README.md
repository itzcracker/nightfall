# Nightfall

Как добавить игру:
1. Папку с игрой положи в `games/` (внутри должен быть `index.html`), например `games/among-us/index.html`.
   Одиночный файл тоже подходит: `games/among-us.html`.
2. Обложку положи в `covers/` с тем же именем: `covers/among-us.png` (png, jpg или webp).
3. Закоммить. Через минуту список игр обновится сам (вкладка Actions).

Название игры берётся из имени папки (`among-us` → «Among Us»).
Чтобы поменять название, открой `games.json` и поправь поле `name`, оно сохранится.

Шрифт: положи `Lufga-Regular.woff2` и `Lufga-Bold.woff2` в папку `fonts/`.

Включить сайт: Settings → Pages → Branch: main, папка / (root).
