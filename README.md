# Pseudorandom number generator (generator liczb pseudolosowych)
>Jawnie grzeszy, kto opowiada o arytmetycznych procedurach generowania liczb losowych. Nie ma bowiem, jak to już nieraz mówiono, czegoś takiego, jak liczba losowa. Istnieją metody losowego wytwarzania liczb, ale oczywiście żadna deterministyczna procedura arytmetyczna nie jest taką metodą. 
>
>John von Neumann, 1951

## Spis treści
* [Wstęp - wymagania projektowe](#wstęp)
* [Opis teoretyczny problemu, rozwiązanie matematyczne](#opis-teoretyczny-problemu)
* [Implementacja rozwiązania (pseudokod)](#implementacja-rozwiązania)
* [Rezultaty działania programu](#rezultaty-działania-programu)
* [Eksperymenty](#eksperymenty)
* [Interpretacja wyników](#interpretacja-wyników)
* [Posłowie](#posłowie)

## Wstęp - wymagania projektowe <a name="wstęp"></a>
Istotą projektu było stworzenie generatora liczb pseudolosowych o rozkładzie równomiernym. Na jego podstawie należało stworzyć generator liczb pseudolosowych dla rozkładu jednostajnego na przedziale (0, 1) - a z kolei na jego bazie - generatory liczb losowych z rozkładów: Bernoulliego, dwumianowego, Poissona, wykładniczego, normalnego.

Zakazane było wykorzystywanie gotowych funkcji lub bibliotek dla generowania liczb losowych. Zakaz obejmował również korzystanie ze źródel pseudolosowych danych typu zegar systemowy.

## Opis teoretyczny problemu, rozwiązania matematyczne <a name="opis-teoretyczny-problemu"></a>
Liczba losowa jest liczbą `r` należącą do pewnego zbioru wartości `{r_1, ..., r_n}` wybieranych z pewnym prawdopodobieństwem. Jeśli jako `r` może pojawić się każda z liczb zbioru z tym samym prawdopodobieństwem `P(r) = 1/n`, to mówimy o równomiernym rozkładzie prawdopodobieństwa liczb losowych z tego zbioru. "Naturalne" liczby losowe wytwarzają się na przykład przy rzucaniu kostką do gry, tasowaniu kart, ciągnieniu losów z urny itp. Generatory takie mają jednak niewielkie zastosowanie praktyczne i mogą być przydatne tylko do losowania niedużych próbek do badań reprezentacyjnych.

###  Liniowy generator kongruencyjny liczb pseudolosowych [ozn. G]:
W 1951 roku Lehmer zaproponował tzw. liniowy generator kongruencyjny liczb pseudolosowych:

> <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;(a&space;x_n&space;&plus;&space;c)&space;\&space;mod&space;\&space;m" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;(a&space;x_n&space;&plus;&space;c)&space;\&space;mod&space;\&space;m" title="x_{n+1} = (a x_n + c) \ mod \ m" /></a>

Jeśli `c = 0`, to otrzymujemy tzw. generator multiplikatywny, w przeciwnym przypadku mówimy o generatorze mieszanym. Domyślnie przyjąłem w rozwiązaniu, że generator jest właśnie multiplikatywny.

Taka metoda sprawia, że otrzymujemy pewien ciąg liczbowy, zależny od początkowych wartości liczb `a`, `c` oraz `m`, który możemy nazwać pseudolosowym.


### Generator liczb pseudolosowych dla rozkładu jednostajnego na przedziale (0, 1) [ozn. U(0, 1)]:

Liczbę pseudolosową otrzymaną jako rezultat działania takiego generatora, otrzymamy poprzez wygenerowanie liczby pseudolosowej z generatora `G` i podzielenie jej przez liczbę `m`. 

Możemy uogólnić wyszukiwanie takich liczb pseudolosowych dla dowolnego przedziału `(e, f)` [ozn. U(e, f)], poprzez pomnożenie liczby wygenerowanej przez `U(0, 1)` przez `(f - e)`, a następnie dodanie do niej liczby `e`.


### Generator liczb losowych z rozkładu Bernoulliego (z parametrem p) [ozn. B(1, p)] i rozkładu dwumianowego [ozn. Bi(p, n)]:

Generator liczb losowych z rozkładu Bernoulliego zwraca 1 lub 0 (sukces/porażka). Najprostszy algorytm generowania zmiennej losowej o rozkładzie dwumianowym, oparty na jej definicji, zwraca właśnie liczbę sukcesów w n próbach w schemacie Bernoulliego.


### Generator liczb losowych z rozkładu Poissona [ozn. P(lamb)]:

Zmienna losowa X ma rozkład Poissona P(lamb), jeżeli `(dla x = 0, 1, ...)`:

> <a href="https://www.codecogs.com/eqnedit.php?latex=P\{X&space;=&space;x\}&space;=&space;\frac{\lambda^x}{x!}&space;e^{-\lambda}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P\{X&space;=&space;x\}&space;=&space;\frac{\lambda^x}{x!}&space;e^{-\lambda}" title="P\{X = x\} = \frac{\lambda^x}{x!} e^{-\lambda}" /></a>

Najprostszy algorytm generowania zmiennej losowej o tym rozkładzie jest oparty na następującym lemacie: niech `(e_0, e_1, ...)` jest ciągiem zmiennych losowych z rozkładu wykładniczego E(0, 1). Wówczas zmienna losowa `X` ma rozkład Poissona `P(lamb)`, gdzie:
> <a href="https://www.codecogs.com/eqnedit.php?latex=X&space;=&space;min&space;\{j:&space;\sum_{i=0}^{j}&space;e_i&space;>&space;\lambda&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X&space;=&space;min&space;\{j:&space;\sum_{i=0}^{j}&space;e_i&space;>&space;\lambda&space;\}" title="X = min \{j: \sum_{i=0}^{j} e_i > \lambda \}" /></a>


### Generator liczb losowych z rozkładu wykładniczego [ozn. E]:
Rozkład wykładniczy – rozkład zmiennej losowej opisujący sytuację, w której oczekujemy na zjawisko całkowicie losowe, mogące zajść w dowolnej chwili `t >= 0`.

Dystybuanta rozkładu E(0, 1) ma postać: `F(x) = 1 - e^{-x}` dla dodatniego x. Wynika stąd prosty sposób generowania liczb losowych o rozkładzie wykładniczym E(0, 1) metodą odwracania dystrybuanty:
> <a href="https://www.codecogs.com/eqnedit.php?latex=X&space;=&space;-ln(U)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X&space;=&space;-ln(U)" title="X = -ln(U)" /></a>

gdzie U jest zmienną losową o rozkładzie równomiernym U(0, 1).


### Generator liczb losowych z rozkładu normalnego [ozn. N]:
Jeden z najważniejszych rozkładów prawdopodobieństwa, odgrywający ważną rolę w statystyce. Wykres funkcji prawdopodobieństwa tego rozkładu jest krzywą w kształcie dzwonu. Przyczyną jego znaczenia jest częstość występowania w naturze.

Do stworzenia tego generatora użyłem kilku metod (w tym metody Marsaglii i Braysa z roku 1964). Jej skomplikowany dowód znajduje się w książce użytej jako źródło projektowe, zaś same algorytmy znajdują się w następnej sekcji.


## Implementacja rozwiązania <a name="implementacja-rozwiązania"></a>
Implementacja rozwiązania w języku Python znajduje się w pliku `main.py`. Zostały użyte pomocnicze moduły/biblioteki takie jak `math`, `numpy`, `matplotlib`. 

Poniżej znajdują się algorytmy zapisane w pseudokodzie pythonopodobnym, na których podstawie jest napisany kod. Obrazują one jak tworzyć dany generator w oparciu o powyższe wprowadzenie matematyczne.

- ### LCG:
```python
[G](a, c=0, m, x0):

    return (a * x0 + c) % m
```

- ### U(0, 1):
```python
[U(e, f)](a, c=0, m, x0):

    g <- [G](a, c, m, x0)
  
    return (g / m) * (f - e) + e
```

- ### B(1, p):
```python
[B(1, p)]:
  
    u <- U(0, 1)
  
    if u <= p:
        return 1
    else:
        return 0
```

- ### Bi(p, n):
```python
[Bi(p, n)]:
  
    x <- 0
  
    for i in (1, ..., n):
        u <- U(0, 1)
        if u <= p:
          x <- x+1
      
    return x
```

- ### P(lamb):
```python
[P(lamb)]:
  
    x <- -1
    s <- 0
    
    while s <= lamb:
      e <- E(0, 1)
      y <- e    
      s <- s + y
      x <- x + 1
    
    return x
```

- ### E:
```python
[E]:
    
    u <- U(0, 1)
    
    return -ln(u)
```

- ### N:
```python
[N1]:  # Marsaglia-Bray
    
    u <- U(0, 1)
    v <- U(0, 1)
    w <- U(0, 1)
    
    p1 <- 16 / sqrt(2*pi*e)
    p2 <- 0.1108179673
    p4 <- 0.0026997960
    p3 <- 1-p1-p2-p4
    c1 <- 17.4973119
    c2 <- 4.73570326
    c3 <- 2.15787544
    c4 <- 2.36785163
    m <- 0.357070192
    
    if 0 <= u <= p1:
        return (2 * u) / p1 - 1 + v + w
    
    if p1 < u <= p1+p2:
        return 1.5 * ((u-p1) / p2 - 1 + v)
        
    if 1-p4 < u <= 1:
        while True:
            x <- 4.5 - ln(w)
          
            if x*v*v > 4.5:
                break
              
        return sqrt(2*x) * sgn(u - (1-p4)/2)
        
    if p1+p2 < u <= 1-p4:
        while True:
            w1 <- U(-3, 3)
            a <- abs(w1)
            w <- (c4 / m) * (3 - a) * (3 - a)
            s <- 0
          
            if a < 1.5:
                s <- (c3 / m) * (1.5 - a)
                
            if a < 1:
                s <- s + (c2 / m) * (3 - a * a) - w
            
            if v > (c1 / m) * e^(-a*a) / 2 - s - w:
                break
        
        return w1
    
    return 0
```

```python
[N]:
    
    while True:
        u <- U(0, 1)
        v <- U(-sqrt(2/e), sqrt(2/e))
        t <- v/u
        
        if u*u > e^(-t*t/2):
            break
            
    return t
```


```python
[N]:
    
    while True:
        u <- E(0, 1)
        v <- U(0, 1)
  
        
        if sqrt(2*e/pi) * w2 * e^(-w1) <= sqrt(2/pi) * e^(-w1*w1/2):
            break
    
    return u
```

