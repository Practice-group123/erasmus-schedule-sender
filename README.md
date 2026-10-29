# erasmus-schedule-sender

[English](#english) | [Русский](#русский)

---

## English

Schedule sender for Erasmus students: pulls the class schedule from Google Drive, parses it and sends it to students.

> TODO: task description

### Requirements
- Python 3.11+
- Git

### Setup
```bash
git clone https://github.com/Practice-group123/erasmus-schedule-sender.git
cd erasmus-schedule-sender

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Configuration
Copy `.env.example` to `.env` and fill in your values.
**Never commit `.env`, API keys, tokens or `credentials.json`.** Ask the team lead for the values.

### Run
```bash
python main.py
```

### Project structure
```
.
├── .github/          # CODEOWNERS, PR template
├── ...               # TODO: describe modules as they appear
├── requirements.txt
└── README.md
```

### Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md) before your first pull request.

Thats not all. I will gradually update the project structure and write the service descriptions later.

---

## Русский

Рассыльщик расписания для студентов Erasmus: забирает расписание занятий из Google Drive, парсит его и отправляет студентам.

> TODO: описание задачи

### Требования
- Python 3.11+
- Git

### Установка
```bash
git clone https://github.com/Practice-group123/erasmus-schedule-sender.git
cd erasmus-schedule-sender

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Настройка
Скопируйте `.env.example` в `.env` и заполните значения.
**Никогда не коммитьте `.env`, API-ключи, токены и `credentials.json`.** Значения спросите у тимлида.

### Запуск
```bash
python main.py
```

### Структура проекта
```
.
├── .github/          # CODEOWNERS, шаблон PR
├── ...               # TODO: описать модули по мере появления
├── requirements.txt
└── README.md
```

### Участие в разработке
Перед первым pull request прочитайте [CONTRIBUTING.md](CONTRIBUTING.md). 

Это еще не все позже буду добвлять и обновлять структуру проэкта, плюсом распишу подробней работу сервиса.  
