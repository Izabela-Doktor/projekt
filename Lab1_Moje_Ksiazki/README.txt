PROJEKT DJANGO: MIĘDZY STRONAMI — STRONA O KSIĄŻKACH

Uruchomienie:
1. Rozpakuj folder Lab1_Moje_Ksiazki.
2. Otwórz folder w VS Code.
3. Otwórz terminal w folderze, w którym znajduje się manage.py.
4. Wpisz:
   python -m pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
5. Otwórz http://127.0.0.1:8000/

Podstrony:
- / — strona główna
- /polecane/ — polecane książki (przykładowe tytuły)
- /gatunki/ — gatunki literackie
- /kontakt/ — kontakt

Projekt zawiera aplikację hobby, widoki, 4 adresy URL, 5 szablonów HTML z dziedziczeniem
base.html, dane przekazywane do szablonów oraz własny CSS.
