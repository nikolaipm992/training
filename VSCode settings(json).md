## 📘 Инструкция по VSCode settings.json
---
## Содержание
- [Введение](#Введение)
- [1. Глобальные](#1.-Глобальные)
- [2. Локальные проекта](#2.-Локальные-проекта)
- [3. Пример (локально)](#3.-Пример-(локально))
 - [3.1 🐍 Python](#3.1-🐍-Python)
 - [3.2 ✍️ Редактор](#3.2-✍️-Редактор)
 - [3.3 🧪 Отладка (Debugging)](#3.3-🧪-Отладка-(Debugging))
 - [3.4 🧩 Расширения](#3.4-🧩-Расширения)
 - [3.5 🖥️ Терминал](#3.5-🖥️-Терминал)

## Введение
settings.json - это файл настроек VSCode, где ты можешь настроить поведение редактора, расширений, горячих клавиш, интерпретаторов, отладчиков, форматирования, и многое другое.

#### 1. Глобальные:
-Нажать комбинацию: Ctrl+Shift+P
-Введи: Preferences: Open User Settings (JSON)

#### 2. Локальные проекта:
-Создать в корне проекта.vscode/settings.json

#### 3. Пример (локально):
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": false,
    "python.conda.activateEnvironment": false,
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "args": ["-ExecutionPolicy", "Bypass"]
        }
    },
    "powershell.powerShellDefaultVersion": "PowerShell 7 (x64)",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": true
    }
}

#### 3.1 🐍 Python
{
  "python.defaultInterpreterPath": "./venv/bin/python", // или "./venv/Scripts/python.exe" (Windows)
  "python.terminal.activateEnvironment": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "python.analysis.typeCheckingMode": "basic"
}

#### 3.2 ✍️ Редактор
{
  "editor.formatOnSave": true,
  "editor.rulers": [80, 120],
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.wordWrap": "on",
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  }
}

#### 3.3 🧪 Отладка (Debugging)
{
  "debug.onTaskErrors": "showErrors",
  "python.debugging.console": "integratedTerminal"
}

#### 3.4 🧩 Расширения
{
  "extensions.autoUpdate": true,
  "extensions.ignoreRecommendations": false
}

#### 3.5 🖥️ Терминал
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-ExecutionPolicy", "Bypass"]
    }
  }
}