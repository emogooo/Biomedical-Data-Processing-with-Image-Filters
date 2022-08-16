# LBP-HOG-Gabor Filtreleri ile Biyomedikal Verilerin İşlenmesi
 Çeşitli görüntü işleme filtrelerinin biyomedikal veriler ile kullanımı

Orijinal Rönten Görüntüsü

![a](https://user-images.githubusercontent.com/58745898/184991383-dcdc47e3-1e49-4415-b896-3c4094bec526.jpg)

Local Binary Pattern

LBP siyah beyaz resimler ile çalışan bir görüntü işleme tekniğidir. Çoğunlukla yüz tespiti, yüz tanıma, obje tespiti ve obje sınıflandırma işlemleri için kullanılır. (2) Bu teknikte görüntü parçalara ayrıldıktan sonra her bir parça için sayısal işlemler yapılıp değerler elde edilir. Elde edilen her bir değer, bölge ağırlık matrisinde karşılık gelen değer ile çarpılır ve yeni bir değer grubu elde edilmiş olur. Elde edilen bu sayı grubu giriş görüntüsünün LBP histogramı olarak adlandırılır. Bu şekilde farklı resimler için elde edilen histogramlar kullanılarak görüntüler arası benzerlikler tespit edilir. (1)

Çalışma Adımları(1)

1.	Giriş görüntüsünü 3x3 matrislere böl. (Siyah beyaz resimlerde bulunan her bir pixel 0-255 değerleri arasındadır. Bu nedenle giriş görüntüsü 3x3 parçalara bölünmektedir.)
2.	Her matrisin değerini hesapla. (Matris değerinin nasıl hesaplandığına yazının devamında değinilmiştir.)
3.	Hesaplanan tüm değerleri sıralı şekilde birleştir ve yeni bir matris oluştur.
4.	Bölgelere ait katsayılar ile her hücreyi çarpıp final matrisini oluştur. (Katsayı matrisinin oluşturulması için ayrıca bir bilimsel çalışma gerekmektedir.)

LBP Bölgesel Hesaplama Yöntemi (2)

![lbpf](https://user-images.githubusercontent.com/58745898/184992767-f76dde8c-b3ae-453d-97b6-0f9f3924af14.png)

gp = n’inci Komşu Pixel Değeri

gc = Merkez Pixel Değeri

Yukarıda belirtilen formül ile oluşturulan yeni değerler 3x3 matrisin, 0-0 hücresinden başlanarak saat yönünde rakamların ardı ardına koyulmasıyla elde edilen 8 bitlik sayı, o matrisin binary değerini temsil etmektedir. Bu binary sayı 10’luk sayı sistemine çevrilerek matrisin ondalık sayı sistemindeki değeri bulunmuş olur.

Global Katsayı Matrisi Nedir? 

Global katsayı matrisi, bir görüntüde bulunan bölgenin önem faktörü değerlerini belirten matristir. Örneğin kadın ile erkek resimlerini ayırt eden LBP destekli bir yazılımda kullanılacak katsayı matrisinde dudak bölgesinin katsayısı yüksekken kulak bölgesinin düşük olmalıdır. Bunun sebebi bir erkek ile kadını dudaklardan ayırt etmek kolayken; kulaklardan ayırt etmenin zor olmasıdır. Dolayısıyla katsayı matrisinde dudak bölgesi ayırt edici bir bölge olduğu için bu bölgenin katsayısının yüksek olması gerekir. (1)

LBP Filtresi ile Röntgen Görüntüsü

![lbp](https://user-images.githubusercontent.com/58745898/184991412-d87a7989-1509-43ce-ac16-379e98f892fe.jpg)

Histogram of Oriented Gradients

HOG, çoğunlukla yüz ve görüntü algılama, yaya algılama, otonom araçlarda gözetim tekniklerinde ve akıllı reklamcılıkta kullanılan görüntü işleme algoritmasıdır. (3) Çalışma prensibi bir nesnenin içerdiği açıları belirleyerek farklı olanları ön plana sürmesidir. Kısacası kenar bulma algoritmalarına benzer bir üslup ile çalışır.

Çalışma Adımları

1.	Özellik Tanımlama: Özellik tanımlayıcı, bir görüntünün temsilidir. Gereksiz bilgileri atarak görüntüyü basitleştirir ve yararlı bilgiler ön plana çıkar. (3)
2.	Ön işleme: Görüntünün ilerideki sorunlarını önlemek için yeniden bir boyutlandırmaya ihtiyacı var. Görüntü herhangi bir boyutta olabilir. Bizim bunu sabit bir en boy oranına getirmemiz gerekiyor. Yaygın olan en boy oranı 1:2'dir, yani görüntüler 100:200, 500:1000… olabilir. (3)
3.	Gradyan Hesaplama: HOG yapmadan önce görüntünün yatay ve dikey gradyanlarının hesaplanması gerekir. Bu durum da görüntünün çekirdek yardımıyla filtrelenmesi ile sağlanır. Kenarlar ve önemli noktalar bulunur. Gauss filtreleme, pencerenin boyutuna bağlı olarak merkezi pikselden uzaklığına göre merkezi piksele en çok ve komşu piksele azalan sırada ağırlık verir. (3)
4.	Gradyanların Histogramını Çıkarma: Görüntü hücrelere bölünür ve her hücre için gradyan histogramı hesaplanır. 8x8 hücreler, 8x8x3 = 192 piksel değerleri içerir. Bu yamanın gradyanı, piksel başına 8x8x2 = 128 sayıya kadar ekleyen 2 değer (büyüklük ve yön) içerir. 8x8 hücre kullanılmasının nedeni özellikleri yakalamak için yeterince büyüktür. (3)
5.	Normalizasyon: Normalizasyon tercihe bağlı olarak yapılabilir. Parlaklık, kontrast ve diğer aydınlatma etkilerinden kaçınmak için kullanılır. (3)
6.	Görüntüyü Görselleştirme: Son olarak bu işlemle bir görüntü elde edilir ve algoritma burada son bulur. (3)

HOG Filtresi ile Röntgen Görüntüsü

![hog](https://user-images.githubusercontent.com/58745898/184991454-c1c98345-fa68-4755-9421-405041c73640.png)

Gabor Filtresi

Gabor Filtresi, görüntü üzerinde belirli yönlerde uzanan ayrıtları tespit etmek için kullanılan bir görüntü işleme filtresidir. Yön temelli bir filtre olduğundan Gabor filtresi plaka tanıma, karakter tanıma, yüz tanıma gibi işlemlerde sıklıkla kullanılır. İşlem çekirdek matris adı verilen bir filtre matrisinin filtrelenecek resim ile konvolüsyonundan ibarettir. Çekirdek matrise ait parametreler aşağıda tek tek incelenmiştir. (4)

Lambda : Kosinüs çarpanının dalga boyunu belirleyen katsayıdır. Katsayının 1 olması durumunda kosinüs ifadesi sürekli 1 olacağından ( cos(2.pi.x') =1) katsayı 2 veya daha büyük bir tamsayı seçilmelidir. (4)

Teta: Teta doğrudan formül içerisinde görünmese de Gabor filtresinin aslında en önemli değişkenlerinden biridir. Bu değişken x' ve y' değerlerinin hesaplanmasında kullanılır ve oluşturulmak istenen Gabor çekirdeğinin yönelim açısıdır. x' ve y' değişkenleri verilen bir teta değeri için aşağıdaki formül ile hesaplanır. (4)

Fi : Fi açısı oluşturulacak çekirdek matrisinin faz açısıdır. Bu değer değiştirilerek filtre x ekseninde ötelenebilir. (4)

Sigma : Sigma değeri Gaussian fonksiyonun standart sapmasını belirleyen katsayıdır. Bu parametre Gaussian fonksiyonun açıklığını belirlediğinden bu değerin küçük seçilmesi ile Gabor dalgacıkları bir birlerine yaklaşacaktır. (4)

Gamma : Bu değer de verilen standart sapma değerinin y' için belirlenmesinin sağlar. Bu değerin 1 olması durumunda oluşacak çekirdek matris x ve y için eşit standart sapmaya sahip olduklarından eşit uzunlukta olacakken, farklı bir oran seçildiğinde çekirdek matris dikdörtgenimsi bir şekilde oluşacaktır. (4)

x,y : Bu iki değer oluşturulacak 2 boyutlu çekirdek matrisin koordinatlarını temsil eder. NxN büyüklükte bir çekirdek matris için x ve y değerleri [-(N-1)/2,(N-1)/2] aralığında gezilerek çekirdek matris hesaplanır. (4)
 

Verilen parametreler ile hesaplanan Gabor çekirdeği doğrudan konvolüsyon almaya uygun değildir. Çünkü hesaplanan değerler ile doğrudan yapılacak bir konvolüsyon işlemi sonucunda çıkacak değerler 0-255 değeri arasında yüksek ihtimalle bulunmayacaktır. Bu nedenle çekirdek matris integrali 0 olacak şekilde normalize edilir. Bu işlem sonrasında hesaplanacak yeni değerlerin pek çoğu 0-255 arasında kalacaktır. (4)

Normalizasyon işlemi çekirdek üzerinde şu adımlarla yapılır. (4)

1.	Pozitif ve Negatif değerlerin toplamlarını hesapla
2.	Bu iki değerin genliklerinin ortalamasını hesapla
3.	px=Pozitif Toplam / Ortalama ve nx=-Negatif Toplam / Ortalama çarpanlarını hesapla
4.	Pozitif değerleri nx, Negatif değerleri ise px katsayısı ile çarp

Gabor Filtresi ile Röntgen Görüntüsü

![gabor](https://user-images.githubusercontent.com/58745898/184991499-39df876e-d0cc-41cd-9347-895069972b56.jpg)
