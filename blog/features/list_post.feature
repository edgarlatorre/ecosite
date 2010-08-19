# language: pt-br

Funcionalidade: Listar artigos
	Para ler um artigo o usuário
	deve ver uma lista contendo os artigos recentes
	
	Cenário: Listando artigos
		Dado que existem 10 artigos publicados
		Quando vou para a página inicial
		Então eu deveria ver a listagem dos artigos