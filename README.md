papadimitriou-book
==================
Os arquivos deste repositório contém implementações em Python dos algoritmos propostos no livro texto do curso, Algorithms (Papadimitriou).

Os primeiros algoritmos tiveram uma implementação direta do pseudocódigo, enquanto outras tiveram que ser adaptadas por conta da linguagem escolhida.

Observa-se principalmente no módulo "algorithms_chaprter02.py" métodos e funções que começam com o prefixo "_", por exemplo "_to_bin". Todos os métodos e funções que começam o esse prefixo são estruturas auxiliares criadas devido a implementação em Python não poder ser uma tradução direta do pseudocódigo, ou como decisão de projeto para algum problema específico não tratado no algoritmo original.
Também está presente no pacote classes de teste para cada módulo, e cada módulo contém os algoritmos de um capítulo.

Os módulos em si não são executados diretamente, apenas contém os algoritmos. Para verificar o funcionamento, recomenda-se a utilização das classes de teste, que além de documentarem diretamente no código os valores esperados para cada entrada, permitem a especificação de um problema específico.

Recomenda-se a utilização de uma IDE, como o Eclipse com o plugin PyDev, para uma execução em Debug passo a passo. Caso deseje, as classes de teste podem ser executadas diretamente com o seguinte comando em uma janela de prompt ou terminal: 
	python test_algorithms_chapter02.py

A seguir, uma lista dos algoritmos implementados por módulo.

1) algorithms_chapter01.py
	multiply
	division
	modeexp
	euclid
	extended_euclid
	primality
	primality2

2) test_algorithms_chapter01.py
 Classe de teste o módulo "algorithms_chapter01.py".

3) algorithms_chapter02.py
	multiply
	merge
	mergesort
	iterative_mergesrot
	selection

4) test_algorithms_chapter02.py
 Classe de teste o módulo "algorithms_chapter02.py".

5) algorithms_chapter02.py
	dfs
	método para obter os componente conexos de um grafo.
	Obs: este módulo contém uma implementação própria de grafos usando lista de adjacências.
Fim.
  
