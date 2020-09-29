# python3
# fab2.py - ローカルで外部ファイルを実行するためのテスト

from fabric.api import local

def iso():
    local("date")