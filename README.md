# 🏎️ F1 Speed Comparison Tool

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![FastF1](https://img.shields.io/badge/using-FastF1-orange)](https://github.com/theOehrly/Fast-F1)

## 📊 Визуализация данных Формулы-1 в реальном времени

Инструмент для анализа и сравнения телеметрических данных гонщиков Формулы-1. Сравнивайте скорость, обороты двигателя и другие параметры на лучших кругах сессий Гран При.

<p align="center">
  <img src="docs/example_plot.png" alt="Пример графика сравнения" width="800"/>
</p>

## ✨ Основные возможности

🏎️ **Сравнение гонщиков** - Визуализация данных двух пилотов на одном графике  
🎨 **Автоматическая стилизация** - Цвета графиков соответствуют цветам команд  
⚡ **Интеллектуальное кэширование** - Быстрая загрузка повторных запросов  
🖥️ **Дружественный интерфейс** - Простой графический ввод параметров  
📈 **Профессиональная визуализация** - Интерактивные графики с сеткой и легендой  

## 🚀 Быстрый старт

### Установка

```bash
# Клонирование репозитория
git clone https://github.com/ваш_логин/f1-speed-comparison.git
cd f1-speed-comparison

# Установка зависимостей
pip install -r requirements.txt
```

### Запуск

```bash
python src/f1_speed_comparison.py
```

## 🎮 Как использовать

### 1. Ввод параметров
- **Год**: 2018-2024
- **Гран При**: Monaco, Silverstone, 1, 7 и т.д.
- **Сессия**: FP1, FP2, FP3, Q (квалификация), R (гонка)
- **Гонщики**: LEC, HAM, VER, NOR, ALO и другие

### 2. Примеры идентификаторов
| Гонщик | Код | Команда |
|--------|-----|---------|
| Шарль Леклер | `LEC` | Ferrari |
| Макс Ферстаппен | `VER` | Red Bull |
| Льюис Хэмилтон | `HAM` | Mercedes |
| Ландо Норрис | `NOR` | McLaren |
| Фернадно Алонсо | `ALO` | Aston Martin |

### 3. Интерактивная работа
После построения графика программа предлагает продолжить анализ других гонщиков.

## 📊 Примеры визуализации

### Сравнение скорости
<p align="center">
  <img src="docs/speed_comparison.png" alt="Сравнение скорости" width="600"/>
</p>

### Анализ телеметрии
<p align="center">
  <img src="docs/telemetry_analysis.png" alt="Анализ телеметрии" width="600"/>
</p>

## ⚙️ Технические особенности

### Кэширование данных
```python
# Автоматическое кэширование для ускорения повторных запросов
cache_dir = 'data/cache/'
fastf1.Cache.enable_cache(cache_dir)
```

### Стилизация графиков
```python
# Автоматические цвета команд
get_driver_style(identifier='LEC', style=['color', 'linestyle'])
```

### Обработка ошибок
- Проверка существования данных
- Валидация ввода пользователя
- Корректная обработка исключений

## 🛠️ Требования

- **Python**: 3.8 или выше
- **Интернет**: Для первой загрузки данных
- **Память**: 500MB свободного места (для кэша)

## 📦 Зависимости

```txt
fastf1>=3.0.0
matplotlib>=3.5.0
numpy>=1.21.0
pandas>=1.3.0
```

## 🔧 Сборка исполняемого файла

```bash
# Установка PyInstaller
pip install pyinstaller

# Создание .exe файла
pyinstaller --onefile --windowed src/f1_speed_comparison.py
```

Результат: `dist/f1_speed_comparison.exe`

## 📁 Структура проекта

```
f1-speed-comparison/
├── src/                    # Исходный код
│   └── f1_speed_comparison.py
├── data/                   # Кэш данных
│   └── cache/
├── docs/                   # Документация
│   ├── example_plot.png
│   └── screenshots/
├── requirements.txt        # Зависимости
├── README.md              # Документация
└── .gitignore             # Игнорируемые файлы
```

## 🤝 Вклад в проект

1. **Форк** репозитория
2. **Создание ветки** (`git checkout -b feature/AmazingFeature`)
3. **Коммит изменений** (`git commit -m 'Add AmazingFeature'`)
4. **Пуш в ветку** (`git push origin feature/AmazingFeature`)
5. **Pull Request**

## ⚠️ Ограничения

- Некоторые исторические данные могут быть неполными
- Требуется стабильное интернет-соединение при первой загрузке
- Некоторые сессии могут не содержать телеметрических данных

## 🙏 Благодарности

- [FastF1](https://github.com/theOehrly/Fast-F1) - за отличную библиотеку данных Формулы-1
- Сообществу Формулы-1 за вдохновение
- Разработчикам matplotlib за мощные инструменты визуализации

## 📄 Лицензия

Проект распространяется под лицензией MIT. Смотрите [LICENSE](LICENSE) для подробностей.

## 📧 Поддержка

Если у вас есть вопросы:
- Создайте [Issue](https://github.com/karvi12/f1-speed-comparison/issues)
- Проверьте [Wiki](https://github.com/karvi12/f1-speed-comparison/wiki)
- Свяжитесь через [Discussions](https://github.com/karvi12/f1-speed-comparison/discussions)
