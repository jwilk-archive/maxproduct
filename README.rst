::

   $ head -n 15 test/forenames.txt
   1114536	Anna
   753586	Maria
   689212	Jan
   678251	Andrzej
   677646	Piotr
   666404	Krzysztof
   632666	Stanisław
   601930	Katarzyna
   585732	Małgorzata
   559412	Agnieszka
   558914	Krystyna
   546970	Barbara
   518939	Tomasz
   503983	Ewa
   490542	Paweł

   $ head -n 5 test/surnames.txt
   220217  Nowak
   131940  Kowalski
   104418  Wiśniewski
   92945   Dąbrowski
   89366   Lewandowski

   $ maxproduct 15 test/forenames.txt test/surnames.txt
   245439774312 Anna Nowak
   165952448162 Maria Nowak
   151776199004 Jan Nowak
   149362400467 Andrzej Nowak
   149229169182 Piotr Nowak
   147051879840 Anna Kowalski
   146753489668 Krzysztof Nowak
   139323808522 Stanisław Nowak
   132555218810 Katarzyna Nowak
   128988143844 Małgorzata Nowak
   123192032404 Agnieszka Nowak
   123082364338 Krystyna Nowak
   120452092490 Barbara Nowak
   116377620048 Anna Wiśniewski
   114279189763 Tomasz Nowak

.. vim:ts=3 sw=3 et
