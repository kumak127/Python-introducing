# python3
# fab3.py - リモートマシンで外部ファイルを実行するテスト

from fabric.api import run

def iso():
    run("date -u")