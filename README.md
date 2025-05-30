Цель работы:
Цель данной лабораторной работы — построить график динамики временных рядов, загруженных из стандартных наборов данных библиотеки `statsmodels`, за определенный промежуток времени. В данной работе анализировался набор данных `copper`, включающий мировое потребление меди, цену на медь и цену на алюминий в период с 1961 по 1970 годы.

Задачи:

1. Ознакомиться с форматом и структурой набора данных `copper`, загружаемого из библиотеки `statsmodels`.
2. Отфильтровать данные в соответствии с заданным временным промежутком.
3. Построить графики временных рядов:

   * Мировое потребление меди (WORLDCONSUMPTION)
   * Цена меди (COPPERPRICE)
   * Цена алюминия (ALUMPRICE)
4. Выполнить визуализацию и оформление графика: добавить подписи осей, легенду, сетку и заголовок.
5. Проанализировать динамику данных на графике.

Инструменты и алгоритмы:

Для выполнения лабораторной работы использовались следующие инструменты и библиотеки:

Язык программирования Python** — основной язык разработки.
Библиотека `statsmodels`** — для загрузки встроенного набора временных рядов `copper`.
Библиотека `matplotlib.pyplot`** — для визуализации временных рядов.

Алгоритм выполнения:

1. Импорт необходимых библиотек.
2. Загрузка набора данных `copper` с помощью `statsmodels.datasets`.
3. Преобразование данных в формат pandas DataFrame.
4. Фильтрация строк по значению поля `YEAR`, оставляя только значения с 1961 по 1970 годы включительно.
5. Построение линий графика для каждого из трех временных рядов.
6. Оформление графика (заголовок, подписи осей, легенда, сетка).
7. Отображение графика с помощью `plt.show()`.

---

Ошибки и их исправления:

В процессе выполнения работы возникли следующие проблемы:

1. Отсутствие библиотеки `statsmodels`:
   При первой попытке запуска кода возникла ошибка импорта из-за отсутствия установленной библиотеки.
   Решение:Установка библиотеки с помощью команды `pip install statsmodels`.

2. Ошибки фильтрации данных:
   В некоторых случаях в других наборах данных поля времени представлены не в явной форме (`YEAR`), а в виде индексов или комбинаций нескольких столбцов. В текущем варианте проблем с фильтрацией по году не возникло.

3. Пустые значения в данных:
   Некоторые значения в рядах могли быть пропущены (NaN).
   Решение: Проверка и визуальное подтверждение корректности данных. В этом наборе пропусков замечено не было.

Выводы:
В ходе выполнения лабораторной работы был успешно загружен и проанализирован набор данных `copper`, охватывающий ключевые экономические показатели меди и алюминия за десятилетний период. Построенные графики показали, как изменялись мировое потребление меди, а также цены на медь и алюминий в период с 1961 по 1970 год.

Использование библиотеки `matplotlib` позволило визуализировать временные ряды в удобной и наглядной форме, а `statsmodels` — быстро получить готовый набор данных для анализа.

Данная работа продемонстрировала навыки работы с временными рядами, визуализации данных и предварительной обработки таблиц с помощью языка Python и популярных аналитических библиотек.
