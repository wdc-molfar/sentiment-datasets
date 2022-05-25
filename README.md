# Репозиторій **"sentiment-datasets"** | Вступ

**Репозиторій `sentiment-datasets` - "Репозиторій, що містить тренувальний та тестовий набори українських, російських та англійських текстових інформаційних повідомлень позитивної та негативної тональності"**, які необхідні для навчання та, відповідно, тестування української, російської та англійської моделей сентимент-аналізу та розпізнавання емоційного забарвлення текстів за допомогою засобів [fastText](https://github.com/facebookresearch/fastText) бібліотеки мови програмування `Python`. Також репозиторій містить скрипти для навчання та тестування моделей засобами [fastText](https://github.com/facebookresearch/fastText).

Якість натренованих моделей, яка виражена через точність та повноту розпізнавання, багато в чому залежить від низки факторів, серед яких є і спосіб формування тренувального корпусу текстів. Ручне формування тренувального набору даних є доволі трудомісткою та вартісною процедурою, яку складно виконати для текстів, віднесених до специфічної тематики. В зв’язку з цим пропонується комбінований підхід, що полягає у використанні простих методів сентимент-аналізу для швидкого формування тренувального набору даних з високою точністю розпізнавання, який в подальшому використовується для тренування моделей машинного навчання. 

Для формування вхідного потоку використовуються великі масиви даних, отриманих за допомогою системи моніторингу новинних повідомлень – [InfoStream](http://infostream.ua/) Інформаійного центру "Електронні вісті". Загалом обсяг таких даних сягає декількох сотень мільйонів документів, які попередньо марковані не лише за мовними ознаками (`українська`, `російська` чи `англійська`), а також – за тональністю (`Good` чи `Bad`) на базі [словникового байєсівського алгоритму](https://doi.org/10.48550/arXiv.0806.2738) з невисокою розподільною здатністю, завдяки якому забезпечується висока швидкость і висока повнота розпізнавання, частково за рахунок зменшення точності. 

Для формування бази даних для машинного навчання та тестування навчених моделей автоматично було обирано ті документи, що мають крайні вагові значення емоційних оцінок, обчислених за допомогою байєсівського алгоритму. Тим самим зменшується повнота, але забезпечується найбільша допустима точність, яку може надати байєсівський алгоритм. 

В результаті автоматичного оброблення новинних повідомлень були сформовані шість масивів даних: `130 тис`. українських повідомлень позитивної та `130 тис.` негативної тональності, `130 тис.` російських повідомлень позитивної та `130 тис.` негативної тональності, `150 тис`. повідомлень позитивної та `150 тис.` повідомлень негативної тональності. Далі на основі цих даних було сформовано три навчальні збалансовані набори для української, російської та англійської мови, що містять в кожному рядку навчальне речення разом з міткою, що розпочинається з префікса `__label__` (`__label__good` чи `__label__bad` для маркування речень позитивної чи негативної тональності відповідно). В результаті були отримані три текстові файли `uk.txt`, `ru.txt` та `en.txt` для відповідно української, російської та англійської мови, що знаходяться у вигляді архівів у директорії [train](https://github.com/wdc-molfar/sentiment-datasets/tree/main/train) цього репозиторія [**`sentiment-datasets`**](https://github.com/wdc-molfar/sentiment-datasets). Ці текстові файли застосовуються як база для подальшого навчання.

Також для оцінки якості навчання моделей окремо були сформовані тестові масиви даних, що не перетинаються з навчальною вибіркою, об’ємом, що не перевищував 10% від об’єму начальної вибірки. Архіви з цими тестовими наборами доступні у директорії [test](https://github.com/wdc-molfar/sentiment-datasets/tree/main/test) цього репозиторія [**`sentiment-datasets`**](https://github.com/wdc-molfar/sentiment-datasets). 

Враховуючи високу швидкість отримання тренувального набору (обчислювальна складність відповідає [байєсівському класифікатору](https://doi.org/10.48550/arXiv.0806.2738) й становить `O(N*k)`, де `k` – кількість перевірочних термінів у словнику, `N` – кількість документів на вході) та якість отриманих моделей, можна вважати, що використання простих та швидких методів сентимент-аналізу для автоматичного формування тренувальних текстових корпусів, має перевагу над ручним формуванням тренувальних наборів, який є дуже трудомістким та ресурсозатратним процесом, і, як показано у проектах [ner-uk](https://github.com/lang-uk/ner-uk/blob/master/doc/README.md) та [tone-dict-uk](https://github.com/lang-uk/tone-dict-uk), ще й вимагає експертної пост-обробки. Крім того об’єми опрацьованих вручну даних поступаються об’єму, що був опрацьований автоматично представленим підходом. Як наслідок, висока швидкість та якість запропонованого комбінованого підходу дає змогу використовувати його для автоматичного формування тематичних моделей розпізнавання тональності текстів, зокрема й тих, що віднесяться до специфічної тематики.

### Зміст
- [Позначення та найменування репозиторія](#name)
- [Програмне забезпечення, що супроводжує репозиторій](#software)
- [Функціональне призначення](#function)
- [Опис логічної структури](#structure)
- [Використовувані технічні засоби](#hardware)
- [Виклик та завантаження](#run)
- [Вхідні дані](#inputdata)
- [Вихідні дані](#outputdata)

<a name="name"></a>
<h2>Позначення та найменування репозиторія</h2>

Репозиторій має позначення **`sentiment-datasets`**.

Повне найменування репозиторія – **"Репозиторій, що містить тренувальний та тестовий набори українських, російських та англійських текстових інформаційних повідомлень позитивної та негативної тональності"**.

<a name="software"></a>
<h2>Програмне забезпечення, необхідне для функціонування програмного модуля</h2>

Для функціонування програмного модуля **`sentiment-analyser`**, написаного мовою програмування `Python`, необхідне наступне програмне забезпечення:

- операційна система сімейства `Windows OS` або `Unix`-подібна
- `python` [v3.6.0](https://www.python.org/downloads/release/python-360/) or newer

```sh
python --version Python 3.6.0
```

пакети:
- `fastText` [v0.9.2](https://github.com/facebookresearch/fastText)

```sh
pip install fastText==0.9.2
```

<a name="function"></a>
<h2>Функціональне призначення</h2>

Програмний модуль **`sentiment-analyser`** містить тренувальний та тестовий набори українських, російських та англійських текстових інформаційних повідомлень позитивної та негативної тональності, які необхідні для навчання та, відповідно, тестування української, російської та англійської моделей сентимент-аналізу та розпізнавання емоційного забарвлення текстів за допомогою засобів [fastText](https://github.com/facebookresearch/fastText) бібліотеки мови програмування `Python`.

Також репозиторій містить скрипти для навчання та тестування моделей засобами [fastText](https://github.com/facebookresearch/fastText).

<a name="structure"></a>
<h2>Опис логічної структури</h2>

Репозиторій **`sentiment-analyser`** складається з частин:
- [`train`](https://github.com/wdc-molfar/sentiment-datasets/tree/main/train) - директорії з тренувальним набором даних, що містить `zip`-архіви тренувальних збалансованих вибірок:
	- `uk.txt.zip`, що складається сумарно із `26000` рядків позитивних та негативних українських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `1,49` ГБ)
	- `ru.txt.zip`, що складається сумарно із `26000` рядків позитивних та негативних російських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `1,44` ГБ)
	- `en.txt.zip`, що складається сумарно із 30000 рядків позитивних та негативних англійських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `895` МБ)
- [test](https://github.com/wdc-molfar/sentiment-datasets/tree/main/test) - директорії з тестовим набором данихщо містить `zip`-архіви тестових збалансованих вибірок:
	- `uk.txt.zip`, що складається сумарно із 26000 рядків позитивних та негативних українських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `162,3` МБ)
	- `ru.txt.zip`, що складається сумарно із 26000 рядків позитивних та негативних російських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `186,5` МБ)
	- `en.txt.zip`, що складається сумарно із 30000 рядків позитивних та негативних англійських інформаційних повідомлень розмічених відповідними мітками `__label__pos` чи `__label__neg` в кінці кожного рядка (загальний обсяг розпакованого файлу - `141,9` МБ)
- `train.py` —  скрипта, що виконує навчання моделі на основі відповідного тренувально набору даних, що знаходиться у вищеописаній дерикторії [`train`](https://github.com/wdc-molfar/sentiment-datasets/tree/main/train)
- `test.py` —  скрипта, що здійснює тестування отриманної моделі на основі відповідного тестового набору даних, що знаходиться у вищеописаній дерикторії [`test`](https://github.com/wdc-molfar/sentiment-datasets/tree/main/test).

Навчання моделей здійснюється засобами [fastText](https://github.com/facebookresearch/fastText) за допомогою функції `fastText.train_supervised()`. Для навчання моделі були налаштовані наступні гіперпараметри: 
``` python
hyper_params = { 
	"lr": 0.35,         # Learning rate
	"epoch": 100,       # Number of training epochs to train for
	"wordNgrams": 3,    # Number of word n-grams to consider during training
	"dim": 155,         # Size of word vectors
	"ws": 5,            # Size of the context window for CBOW or skip-gram
	"minn": 3,          # Min length of char ngram
	"maxn": 20,         # Max length of char ngram
	"bucket": 2014846,  # Number of buckets
	}
```
Кількість циклів навчання – `100`, кількість слів у n-грамах – `3`, розмірність вектора моделі – `155`, розмір контекстного вікна – `5`, найменша допустима кількість символів в слові – `3`, найбільша – `20`.

Для одержання стисненої квантованої моделі був використаний метод `quantize` функціоналу [fastText](https://github.com/facebookresearch/fastText) з наступними параметрами квантування:
``` python
model.quantize(
	input=None,
	qout=False,
	cutoff=0,
	retrain=False,
	epoch=None,
	lr=None,
	thread=None,
	verbose=None,
	dsub=2,
	qnorm=False,
	)
```
Після процедури квантування модель зберігається у директорії `models` у файлі формату `.ftz`.


<a name="run"></a>
<h2>Виклик та завантаження</h2>

Для навчання/тестування української, російської чи англійської моделі сентимент аналізу на базі відповідних тренувальних/тестових наборів даних, що описані вище, необхідно:
1. Клонувати репозиторій:
```sh
git clone https://github.com/wdc-molfar/sentiment-datasets.git
```
2. Розпакувати відповідний навчальний/тестовий архів (`uk.txt.zip`, `ru.txt.zip` чи `en.txt.zip`) у дерикторію [`train`](https://github.com/wdc-molfar/sentiment-datasets/tree/main/train) чи [`test`](https://github.com/wdc-molfar/sentiment-datasets/tree/main/test), відповідно.
3. Відкрити командний рядок, перейти в директорію зі склонованим репозиторієм та запустити скрипт `train.py` чи `test.py` для, відповідно, навчання чи тестування моделі сентимент-аналізу, вказавши необхідні додаткові параметри `<lang>` - мову моделі (`uk`, `ru` чи `en`):

```sh
cd fullpath/.../sentiment-datasets
python train.py <lang>
```
або 
```sh
cd fullpath/.../sentiment-datasets
python test.py <lang>
```
Операція може використовуватися як в операційній системі `Windows OS`, так і в `Unix`-подібних системах.

В результаті запуску скрипта `train.py` репозиторія **`sentiment-datasets`**  здійснюється навчання вказаної моделі для сентимент аналізу, подальше її квантування та збереження у директорії `models` у файлі формату `.ftz`.

В результаті запуску скрипта `test.py` репозиторія **`sentiment-datasets`**  здійснюється тестування вказаної моделі для сентимент аналізу та вивід результату тестування у вигляді:
```sh
accuracy: 0.9898675496688741

__label__pos {'precision': 0.9888962326503635, 'recall': nan, 'f1score': 1.977792465300727}
__label__neg {'precision': 0.9908427339084274, 'recall': nan, 'f1score': 1.9816854678168547}
```

## Copyright
Copyright © 2022 [WDC-MOLFAR](https://github.com/wdc-molfar)

