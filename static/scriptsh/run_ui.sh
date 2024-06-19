##!/bin/bash
#
#cd ~/PycharmProjects/Portfolio_S_Borozna
#source .venv/Scripts/activate
#
## shellcheck disable=SC1012
## shellcheck disable=SC1001
#pytest -v -s C:/Users/Светлана/PycharmProjects/Portfolio_S_Borozna/tests

# shellcheck disable=SC1128
# shellcheck disable=SC1128
#!/bin/bash

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")
cd ~/PycharmProjects/Portfolio_S_Borozna
source .venv/Scripts/activate
# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE="C:/Users/Светлана/PycharmProjects/Portfolio_S_Borozna/tests"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../reports"

# Запускаем pytest с использованием относительного пути к файлу test_my_project.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"