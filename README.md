papadimitriou-book
==================
Os arquivos deste reposit�rio cont�m implementa��es em Python dos algoritmos propostos no livro texto do curso, Algorithms (Papadimitriou).

Os primeiros algoritmos tiveram uma implementa��o direta do pseudoc�digo, enquanto outras tiveram que ser adaptadas por conta da linguagem escolhida.

Observa-se principalmente no m�dulo "algorithms_chaprter02.py" m�todos e fun��es que come�am com o prefixo "_", por exemplo "_to_bin". Todos os m�todos e fun��es que come�am o esse prefixo s�o estruturas auxiliares criadas devido a implementa��o em Python n�o poder ser uma tradu��o direta do pseudoc�digo, ou como decis�o de projeto para algum problema espec�fico n�o tratado no algoritmo original.
Tamb�m est� presente no pacote classes de teste para cada m�dulo, e cada m�dulo cont�m os algoritmos de um cap�tulo.

Os m�dulos em si n�o s�o executados diretamente, apenas cont�m os algoritmos. Para verificar o funcionamento, recomenda-se a utiliza��o das classes de teste, que al�m de documentarem diretamente no c�digo os valores esperados para cada entrada, permitem a especifica��o de um problema espec�fico.

Recomenda-se a utiliza��o de uma IDE, como o Eclipse com o plugin PyDev, para uma execu��o em Debug passo a passo. Caso deseje, as classes de teste podem ser executadas diretamente com o seguinte comando em uma janela de prompt ou terminal: 
	python test_algorithms_chapter02.py

A seguir, uma lista dos algoritmos implementados por m�dulo.

1) algorithms_chapter01.py
	multiply
	division
	modeexp
	euclid
	extended_euclid
	primality
	primality2

2) test_algorithms_chapter01.py
 Classe de teste o m�dulo "algorithms_chapter01.py".

3) algorithms_chapter02.py
	multiply
	merge
	mergesort
	iterative_mergesrot
	selection

4) test_algorithms_chapter02.py
 Classe de teste o m�dulo "algorithms_chapter02.py".

5) algorithms_chapter02.py
	dfs
	m�todo para obter os componente conexos de um grafo.
	Obs: este m�dulo cont�m uma implementa��o pr�pria de grafos usando lista de adjac�ncias.
Fim.
  
