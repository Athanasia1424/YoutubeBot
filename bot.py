import os
import subprocess
import sys

# プロジェクトフォルダに移動
project_path = r"C:\Users\nyuza\OneDrive\デスクトップ\a\bot"
os.chdir(project_path)

# venv作成
subprocess.run([sys.executable, "-m", "venv", "venv"])

# 仮想環境の python.exe を使って pip install
venv_python = os.path.join(project_path, "venv", "Scripts", "python.exe")
subprocess.run([venv_python, "-m", "pip", "install", "discord.py"])

# a.py を仮想環境で実行
subprocess.run([venv_python, "a.py"])
