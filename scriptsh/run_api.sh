##!/bin/bash
#ls
#pwd
#pytest -v -s /C/Users/User/PycharmProjects/my_diplom_project/scriptsh

cd ~\PycharmProjects\my_diplom_project
 . .venv\Scripts\Activate.ps1
 python -m pytest --alluredir C:\Users\User\PycharmProjects\my_diplom_project\allure_reports
 pytest -v -s "C:\Users\User\PycharmProjects\my_diplom_project\page_test\tests_belavia.ps1"
