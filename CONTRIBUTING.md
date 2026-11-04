# Zasady Współpracy
Aby nasza współpraca pomyślnie, proszę zastosować się do naszych wyznaczonych zasad!

## Przygotowanie projektu
-Sforkuj repozytorium na swoje konto GitHub.
-Sklonuj swój fork na lokalny komputer (git clone <url>).
-Skonfiguruj zdalne repozytorium, aby móc łatwo pobierać aktualizacje z głównego projektu.

1. Sklonuj repozytorium na swój komputer
   ```bash
git clone https://github.com/user/repo.git
```
2. Przejdź do katologu projektu
``` bash
cd REPO
```

3. Utwórz wirtualne środowisko
```bash
python -m venv .venv
```
4. Aktywuj środowisko i zainstaluj zależności, jeżeli projekt zawiera plik requirements.txt
```bash
.venv\Scripts\Active.ps1
```
```bash
pip install -r requirements.txt
```

## Praca z gałęziami
-Nigdy nie pisz kodu bezpośrednio na gałęzi main.
-Twórz osobne gałęzie dla każdego zadania lub poprawki.
-Stosuj czytelne nazewnictwo gałęzi, np.:
feature/nazwa-funkcjonalności (dla nowych funkcji)
bugfix/opis-błędu (dla poprawy błędów)

## Zasady pisania kodu
-Pisz czysty, czytelny i zrozumiały kod w języku Python.
-Staraj się przestrzegać standardów PEP 8.
-Dodawaj zwięzłe komentarze tam, gdzie logika kodu może nie być oczywista (szczególnie ważne dla osób uczących się!).

## Commity
-Pisz krótkie, opisowe wiadomości commitów w języku angielskim lub polskim.
-Dobry commit odpowiada na pytanie: Co i dlaczego zostało zmienione? (np. Add simple calculator function, Fix typo in main.py).

```bash
git commit -m"feat: dodaj zadanie..."
git commit -m"fix popraw element input"
git commit -m"docs: zaktualizuj readme.md"

## Zgłoszenia (Issues)-


## Pull Requests-
...

## Komunikacja w zespole
-Bądźmy dla siebie życzliwi i pomocni – to projekt stworzony do nauki i rozwoju!
-W razie pytań lub problemów śmiało korzystaj z sekcji komentarzy lub zgłoszeń.

**Dziękujemy za współpracę i wkład w rozwój projektu!**
