# funkcjonalność tylu zrób coś
import os

# polecenie bez możliwości parasowania wyniku
os.system()

# bieżący katalog
os.getcwd()

os.remove()
os.chdir()
os.replace()
os.chmod()
os.chown()
# zmienne środowiskowe
os.environ()

os.getlogin()
os.getgid()
os.getpid()

# sygnał systemowy
os.kill()
# obsługa sygnałów systemowych

import signal
# signal.signal()

os.rmdir()

# informacyjnie - dostęp do informacji

import sys

sys.path
# parametry uruchomieniowe
sys.argv

sys.api_version
sys.getwindowsversion()
# linux/win
sys.platform
#strumienie
sys.stdout
# wersja pythona
sys.version

import shutil
shutil.copy()
shutil.move()
shutil.copytree()
shutil.disk_usage()
shutil.rmtree()
shutil.which()

# operacje na ścieżkach
import os.path
os.path.isfile()
os.path.isdir()

import pathlib
# ścieżka do bieżącego pliku
p = pathlib.Path(__file__)

# katalog bieżącego pliku
k = p.parent.resolve()
# jak otworzyć plik zasoby.txt z tego samego katalogu co skrypt .py
f_path = pathlib.Path(__file__).parent.resolve() / 'zasoby.txt'
print(f_path)

import glob
# wyszukiwanie plików
print(glob.glob('*.py'))

# rekurencyjny spacer po podkatalogach:
for katalog, lista_podkatalogow, lista_plikow in os.walk('.'):
    print(katalog)

