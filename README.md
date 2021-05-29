# Pseudorandom number generator (generator liczb pseudolosowych)
## Spis treści
* [Wstęp - wymagania projektowe](#wstęp)
* [Opis teoretyczny problemu](#opis-teoretyczny-problemu)
* [Rozwiązania matematyczne](#rozwiązania-matematyczne)
* [Implementacja rozwiązania](#implementacja-rozwiązania)
* [Rezultaty działania programu](#rezultaty-działania-programu)
* [Eksperymenty](#eksperymenty)
* [Interpretacja wyników](#interpretacja-wyników)
* [Posłowie](#posłowie)

## Wstęp - wymagania projektowe <a name="wstęp"></a>
Istotą projektu było stworzenie generatora liczb pseudolosowych o rozkładzie równomiernym. Na jego podstawie należało stworzyć generator liczb pseudolosowych dla rozkładu jednostajnego na przedziale (0, 1) - a z kolei na jego bazie - generatory liczb losowych z rozkładów: Bernoulliego, dwumianowego, Poissona, wykładniczego, normalnego.

Zakazane było wykorzystywanie gotowych funkcji lub bibliotek dla generowania liczb losowych. Zakaz obejmował również korzystanie ze źródel pseudolosowych danych typu zegar systemowy.
