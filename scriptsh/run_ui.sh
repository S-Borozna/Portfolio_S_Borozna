#!/bin/bash
wsl
# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")
# shellcheck disable=SC2164
cd ~/PycharmProjects/Portfolio_S_Borozna
source .venv/Scripts/activate
# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE="$SCRIPT_DIR/../tests"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../reports"

# Запускаем pytest с использованием относительного пути к файлу test_my_project.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"