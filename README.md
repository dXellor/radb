# radb
RaDb

<br>
<h2>Šta je RaDb?</h2>
<p style="font-size:large">RaDb je web aplikacija koja služi za sortiranje i rangiranje studenata druge godine smera Računarstvo i automatika sa Fakulteta
    tehničkih nauka u Novom Sadu u odnosu na njihove izabrane module koje žele da pohađaju u trećoj i četvrtoj godini fakulteta.
</p>

<h2>Kako aplikacija funkcioniše?</h2>
<p style="font-size:large">Student koji pohađa smer Računarstvo i automatika se <a href = {% url 'register' %} style="color: #21ba45;">registruje</a> sa svojim UNS emailom na koji
    će, ako su sva polja u formi popunjena kako je naloženo, doći email sa aktivacionim linkom koji je potreban kako bi student mogao da se uloguje na svoj nalog.
</p>
<p style="font-size:large">
    Nakon uspešnog logovanja student će biti redirektovan na stranicu "profil" na kojoj se nalaze njegovi osnovni podaci kao što su broj indeksa, ime i prezime i slično.
    Na toj stranici se takođe nalaze forma za odabir željenih modula, realizovana sa dve dropdown liste i forma sa predmetima i ocenama (indeks) koje student treba da popuni.
    Student takođe ima opciju da sakrije svoje informacije (broj indeksa, ime i prezime) ako ne želi da njegovo rangiranje i željeni moduli budu vidljivi na rang listama 
    (u tom slučaju korisnik se prikazuje kao "Skriveni korisnik").
</p>
<p style="font-size:large">
    Na kraju, na stranici "rang liste" student može da vidi na koju želju je upao kao i da vidi
    svoju i poziciju drugih studenata na rang listi svakog modula.
</p>

<h2>Kako je projekat izrađen?</h2>
<p style="font-size:large">
    Projekat je izrađen u <a href="https://www.djangoproject.com/" style="color: #21ba45;">django framework-u</a>, u python programskom jeziku (backend) i uz pomoć JavaScript-a, HTML-a i CSS-a (frontend).
    Podaci se čuvaju u MySQL bazi podatka. Projekat je razdvojen u dve celine: aplikacija za logovanje i registraciju korisnika i aplikacija za obradu i prikaz podatka.
</p>
<p style="font-size:large">
    Autor ovog projekta je Nikola Simić, student druge godine osnovnih akademskih studija, smer Računarstvo i automatika na Fakultetu tehničkih nauka u Novom Sadu.
</p>

<h2>Zahvalnica</h2>
<p style="font-size:large">
    Zahvaljujem se profesorima sa <a href="https://pilab021.com/" style="color: #21ba45;">PiLab sekcije</a> iz Elektrotehničke škole "Mihajlo Pupin" iz Novog Sada na obezbeđenom hostingu kao i svojim kolegama na
    savetima i pomoći u testiranju aplikacije
</p>