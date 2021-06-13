# Pseudorandom number generator (generator liczb pseudolosowych)
>Jawnie grzeszy, kto opowiada o arytmetycznych procedurach generowania liczb losowych. Nie ma bowiem, jak to już nieraz mówiono, czegoś takiego, jak liczba losowa. Istnieją metody losowego wytwarzania liczb, ale oczywiście żadna deterministyczna procedura arytmetyczna nie jest taką metodą. 
>
>John von Neumann, 1951

## Spis treści
* [Wstęp - wymagania projektowe](#wstęp)
* [Opis teoretyczny problemu, rozwiązanie matematyczne](#opis-teoretyczny-problemu)
* [Implementacja rozwiązania (pseudokod)](#implementacja-rozwiązania)
* [Rezultaty działania programu i eksperymenty](#rezultaty-działania-programu)
* [Interpretacja wyników](#interpretacja-wyników)
* [Posłowie](#posłowie)

## Wstęp - wymagania projektowe <a name="wstęp"></a>
Istotą projektu było stworzenie generatora liczb pseudolosowych o rozkładzie równomiernym. Na jego podstawie należało stworzyć generator liczb pseudolosowych dla rozkładu jednostajnego na przedziale (0, 1) - a z kolei na jego bazie - generatory liczb losowych z rozkładów: Bernoulliego, dwumianowego, Poissona, wykładniczego, normalnego.

Zakazane było wykorzystywanie gotowych funkcji lub bibliotek di generowania liczb losowych. Zakaz obejmował również korzystanie ze źródeł pseudolosowych danych typu zegar systemowy.

Gotowe generatory należało przetestować dowolnym testem typu: chi-kwadrat, Kołmogorova itp.

## Opis teoretyczny problemu, rozwiązania matematyczne <a name="opis-teoretyczny-problemu"></a>
Liczba losowa jest liczbą `r` należącą do pewnego zbioru wartości `{r_1, ..., r_n}` wybieranych z pewnym prawdopodobieństwem. Jeśli jako `r` może pojawić się każda z liczb zbioru z tym samym prawdopodobieństwem `P(r) = 1/n`, to mówimy o równomiernym rozkładzie prawdopodobieństwa liczb losowych z tego zbioru. "Naturalne" liczby losowe wytwarzają się na przykład przy rzucaniu kostką do gry, tasowaniu kart, ciągnieniu losów z urny itp. Generatory takie mają jednak niewielkie zastosowanie praktyczne i mogą być przydatne tylko do losowania niedużych próbek do badań reprezentacyjnych. Powody są oczywiste: ciężko o wygenerowanie wielu wyników rzutu kością czy wytworzenie tysięcy rezultatów w skutek loterii liczbowej.

###  Liniowy generator kongruencyjny liczb pseudolosowych [ozn. G]:
W 1951 roku Lehmer zaproponował tzw. liniowy generator kongruencyjny liczb pseudolosowych:

> <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;(a&space;x_n&space;&plus;&space;c)&space;\&space;mod&space;\&space;m" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;(a&space;x_n&space;&plus;&space;c)&space;\&space;mod&space;\&space;m" title="x_{n+1} = (a x_n + c) \ mod \ m" /></a>

Jeśli `c = 0`, to otrzymujemy tzw. generator multiplikatywny, w przeciwnym przypadku mówimy o generatorze mieszanym. Domyślnie przyjąłem w rozwiązaniu, że generator jest właśnie multiplikatywny.

Taka metoda sprawia, że otrzymujemy pewien ciąg liczbowy, zależny od początkowych wartości liczb `a`, `c` oraz `m`, który możemy nazwać pseudolosowym. Istnieją wartości tych parametrów, które umożliwiają generowanie dużej liczby unikalnych liczb pseudolosowych, zostaną one użyte jako domyślne w implementacji tego generatora.


### Generator liczb pseudolosowych dla rozkładu jednostajnego na przedziale (0, 1) [ozn. U(0, 1)]:

Liczbę pseudolosową otrzymaną jako rezultat działania takiego generatora, otrzymamy poprzez wygenerowanie liczby pseudolosowej z generatora `G` i podzielenie jej przez liczbę `m`. 

Możemy uogólnić wyszukiwanie takich liczb pseudolosowych dla dowolnego przedziału `(e, f)` [ozn. U(e, f)], poprzez pomnożenie liczby wygenerowanej przez `U(0, 1)` przez `(f - e)`, a następnie dodanie do niej liczby `e`.

Rozkład `U` jest bardzo przydatny do tworzenia innych popularnych rozkładów liczb losowych, niemalże każdy algorytm ich generacji, opiera się na wytworzeniu liczb z `U(0, 1)`, a następnie na operacji na nich. Z tego względu, wyniki wszystkich rozkładów są bardzo zależne od generatora `G`, a więc w szczegolności od jej parametrów.

### Generator liczb losowych z rozkładu Bernoulliego (z parametrem p) [ozn. B(1, p)] i rozkładu dwumianowego [ozn. Bi(p, n)]:

Generator liczb losowych z rozkładu Bernoulliego zwraca 1 lub 0 (sukces/porażka). 

Rozkład dwumianowy to z definicji dyskretny rozkład prawdopodobieństwa opisujący liczbę sukcesów *k* w ciągu *N* niezależnych prób, z których każda ma stałe prawdopodobieństwo sukcesu równe *p*.

### Generator liczb losowych z rozkładu Poissona [ozn. P(lamb)]:

Rozkład Poissona to z definicji dyskretny rozkład prawdopodobieństwa, wyrażający prawdopodobieństwo szeregu wydarzeń mających miejsce w określonym czasie, gdy te wydarzenia występują z dną średnią częstotliwością i w sposób niezależny od czasu jaki upłynął od ostatniego zajścia takiego zdarzenia. 

Zmienna losowa X ma rozkład Poissona `P(lamb)`, jeżeli `(dla x = 0, 1, ...)`:

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

```python
[N]:    # Box-Muller   
    
    u1 <- U(0, 1)
    u2 <- U(0, 1)
  
    a <- 2 * pi * u2
    p <- sqrt(-2 * ln(u1))
    
    return (p * cos(a))
```

```python
[N]:    # polar method
    
    while True:
        u1 <- E(0, 1)
        u2 <- U(0, 1)
        v1 <- 2 * u1 - 1
        v2 <- 2 * u2 - 1
        w <- v1 * v1 + v2 * v2
        
        if w >= 1:
            break
    
    return (v1 * (-2 * ln(w) / w))
```

## Rezultaty działania programu i eksperymenty <a name="rezultaty-działania-programu"></a>
Założenia: wygenerowano po 10000 danych z każdego generatora. Rezultat został przedstawiony na graficznych histogramach - mogą one stanowić pierwszy (mało matematyczny) test poprawności działania generatorów, ponieważ przedstawiają rozłożenie danych. 

Jako że działanie generatorów opiera się na głównym generatorze G, to ważną rolę pełnią parametry początkowe. Do budowania histogramu przyjęto wartości używane np. w C++11 (minstd_rand): `a = 48271, m = 2147483647, c = 0, x0 = 1`.

- ### G(48271, 2147483647, 0, 1)
![lcg](/Histograms/lcg.png "LCG")

- ### U(0, 1)
![u](/Histograms/u(0,1).png "U(0, 1)")

- ### B(0.6)
![b](/Histograms/bernoulli.png "B(0.6)")

- ### Bi(0.7, 100)
![bi](/Histograms/binomial.png "Bi(0.7, 100)")

- ### P(3)
![p](/Histograms/poisson.png "P(3)")

- ### E
![e](/Histograms/expo.png "E(0, 1)")

- ### N
![n](/Histograms/normal.png "N")

### Testowanie
Jednym z czynników składających się na całość projektu było testowanie generatorów. 

Posłużyłem się testami chi-kwadrat. Test chi-kwadrat służy do sprawdzenia, czy próbka danych pochodzi z grona populacji o określonym rozkładzie. W przypadku obliczenia jakości dopasowania chi-kwadrat dane są podzielone na k przedziałów, a statystyka testowa jest zdefiniowana jako:
> <a href="https://www.codecogs.com/eqnedit.php?latex=\chi^2&space;=&space;\sum_{i=1}^k&space;\frac{(O_i&space;-&space;E_i)^2}{E_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\chi^2&space;=&space;\sum_{i=1}^k&space;\frac{(O_i&space;-&space;E_i)^2}{E_i}" title="\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}" /></a>

gdzie `O_i` oznacza obserowaną częstotliwość dla i, z kolei `E_i` oczekiwaną częstotliwość obliczną ze wzoru:
> <a href="https://www.codecogs.com/eqnedit.php?latex=E_i&space;=&space;N(F(Y_b)&space;-&space;F(Y_a))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_i&space;=&space;N(F(Y_b)&space;-&space;F(Y_a))" title="E_i = N(F(Y_b) - F(Y_a))" /></a>

gdzie `F` to dystrybuanta testowanej dystrybucji, Y_b jest górną granicą klasy, Y_a dolną granicą, a N jest wielkością tablicy z danymi (ilością danych). 

Ilość "pojemników" nie jest z góry określona, wiele źródeł podaje optymalną ich ilość jako `2(N^(0.4))` - właśnie taka wartość domyślna jest używana w implementacji tego projektu.

Odrzucamy hipotezę, że dane pochodzą z populacji o danym rozkładzie, jeśli:
> <a href="https://www.codecogs.com/eqnedit.php?latex=\chi^2&space;>&space;\chi^2_{1-a,&space;k-c}&space;=&space;P" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\chi^2&space;>&space;\chi^2_{1-a,&space;k-c}&space;=&space;P" title="\chi^2 > \chi^2_{1-a, k-c} = P" /></a>

gdzie `P` oznacza wartość krytyczną chi-kwadrat dla k-c stopni swobody i pewnym poziomem istotności `a` (w niniejszym programie przyjęto, że `a = 0.05`).

#### Sposób testowania w Pythonie:
Funkcja do testowania chi kwadrat przyjmuje jako argumenty: dane do sprawdzenia (wygenerowane przed dany rozkład) oraz dystrybuantę z danego rozkładu, który sprawdzamy.


Tworzymy tablicę z przykładowymi danymi o danym rozkładzie, określamy funkcję `cdf` z modułu `scipy.stats` o danym rozkładzie (czyli `scipy.stats.XYZ.cdf(arg)`, przykładowo: `scipy.stats.bernoulli(k, p=0.6)`. Jest to nic innego jak *cumulative distribution function* - dystrybuanta. 

Do testowania użyto 10000 danych wejściowych, generator G z argumentami używanymi powyżej. 
`True` - test zaliczony, `False` - test niezaliczony.

#### Testowanie rozkładu Bernoulliego:
```python
    data = [B.__next__(0.6) for _ in range(10000)]
    cdf = lambda x: scipy.stats.bernoulli.cdf(k=x, p=0.6)
    print(t.chi_square(data, cdf))
    
    # True
```
#### Testowanie rozkładu dwumianowego:
```python
    data = [Bi.run(0.7, 100) for _ in range(10000)]
    cdf = lambda x: scipy.stats.binom.cdf(k=x, p=0.7, n=100)
    print(t.chi_square(data, cdf))
    
    # True
```
#### Testowanie rozkładu Poissona:
```python
    data = [P.run(3) for _ in range(10000)]
    cdf = lambda x: scipy.stats.poisson.cdf(k=x, mu=3)
    print(t.chi_square(data, cdf))
    
    # True
```

#### Testowanie rozkładu wykładniczego:
```python
    data = [E.run() for _ in range(100000)]
    cdf = lambda u: scipy.stats.expon.cdf(x=u)
    print(t.chi_square(data, cdf))
    
    # False (np. dla x0 = 1)
    # True (np. dla x0 = 3)
```
#### Testowanie rozkładu normalnego:
```python
    data = [N.r4() for _ in range(10000)]
    cdf = lambda u: scipy.stats.norm.cdf(x=u)
    print(t.chi_square(data, cdf))
    
    # True
```

## Interpretacja wyników <a name="interpretacja-wyników"></a>
Generalnie można uznać testowanie projektowych generatorów jako pozytywną weryfikację ich wyników. Jednakże warto wspomnieć o tym, że ilość danych nie jest wystarczająca do wiarygodnego testowania. Poza tym, wpływ na rezultat działania generatorów ma przede wszystkim główny generator G, w szczególności jego argumenty `a, m, x0`. Widać to doskonale dla powyższego testowania generatora E. Dla `x0 = 1` test jest nieudany, z kolei dla innego przykładowego `x0 = 3`, test został zaliczony pomyślnie.
Poprawność uzyskanych wyników pokazują również wykresy, których wygląd pokrywa się z prawidłowym zachowaniem "funkcji" utworzonych przez punkty wygenerowane z danego rozkładu.

Reasumując, całość projektu można uznać za zakończoną. Poprawność bierze się również w udowodnionych dawniej lematach, twierdzeniach i spostrzeżeniach, które sprawiają, że można było wykorzystać generator `G` do wytworzenia generatorów innych rozkładów poprawnie.

## Posłowie <a name="posłowie"></a>
Projekt został wykonany na potrzeby kursu "Rachunek prawdopodobieństwa i statystyka" na Uniwersytecie Jagiellońskim.

### Źródła projektowe:
* Wieczorkowski Robert, "Komputerowe generatory liczb losowych"
* Ross Sheldon, "A first course in probability"
* Wałaszek Jerzy, I Liceum Ogólnokształcące im. K. Brodzińskiego w Tarnowie: https://eduinf.waw.pl/
* National Institute of Standards and Technology: https://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm
