#!/usr/bin/python
# -*- coding: utf-8 -*-

from textteaser import TextTeaser

# article source: https://blogs.dropbox.com/developers/2015/03/limitations-of-the-get-method-in-http/
title = "Limitations of the GET method in HTTP"
text = "We spend a lot of time thinking about web API design, and we learn a lot from other APIs and discussion with their authors. In the hopes that it helps others, we want to share some thoughts of our own. In this post, we’ll discuss the limitations of the HTTP GET method and what we decided to do about it in our own API.  As a rule, HTTP GET requests should not modify server state. This rule is useful because it lets intermediaries infer something about the request just by looking at the HTTP method.  For example, a browser doesn’t know exactly what a particular HTML form does, but if the form is submitted via HTTP GET, the browser knows it’s safe to automatically retry the submission if there’s a network error. For forms that use HTTP POST, it may not be safe to retry so the browser asks the user for confirmation first.  HTTP-based APIs take advantage of this by using GET for API calls that don’t modify server state. So if an app makes an API call using GET and the network request fails, the app’s HTTP client library might decide to retry the request. The library doesn’t need to understand the specifics of the API call.  The Dropbox API tries to use GET for calls that don’t modify server state, but unfortunately this isn’t always possible. GET requests don’t have a request body, so all parameters must appear in the URL or in a header. While the HTTP standard doesn’t define a limit for how long URLs or headers can be, most HTTP clients and servers have a practical limit somewhere between 2 kB and 8 kB.  This is rarely a problem, but we ran up against this constraint when creating the /delta API call. Though it doesn’t modify server state, its parameters are sometimes too long to fit in the URL or an HTTP header. The problem is that, in HTTP, the property of modifying server state is coupled with the property of having a request body.  We could have somehow contorted /delta to mesh better with the HTTP worldview, but there are other things to consider when designing an API, like performance, simplicity, and developer ergonomics. In the end, we decided the benefits of making /delta more HTTP-like weren’t worth the costs and just switched it to HTTP POST.  HTTP was developed for a specific hierarchical document storage and retrieval use case, so it’s no surprise that it doesn’t fit every API perfectly. Maybe we shouldn’t let HTTP’s restrictions influence our API design too much.  For example, independent of HTTP, we can have each API function define whether it modifies server state. Then, our server can accept GET requests for API functions that don’t modify server state and don’t have large parameters, but still accept POST requests to handle the general case. This way, we’re opportunistically taking advantage of HTTP without tying ourselves to it."

tt = TextTeaser()
sentences = tt.summarize(title, text)
for sentence in sentences:
  print(sentence)

title = "Será que a Bel Pesce aprendeu mesmo a lição?"
text = """
Quando decidi escrever e buscar ser uma referência sobre empreendedorismo, conversei com um amigo e ele foi duro comigo — agradeço — dizendo que eu não deveria falar de algo que eu nunca tive grandes êxitos. Por questões de autoridade, eu não deveria querer ser uma referência, antes de ser uma, mesmo tendo uma faculdade de administração e um MBA em gestão estratégica de empresas, alguns negócios testados, tendo passado e contribuído em mais de 250 empresas, eu não tinha um respaldo para solidificar minha fala. Foi ali que eu mudei o discurso de “faça isso”, para “eu tento fazer isso.” E isso não garante nada, falar de empreendedorismo e inovação sem ter nada (ainda) grandioso para mostrar a respeito é frágil demais.
E aqui entra o marketing.
Bel Pesce fez seu nome por ter estudado no MIT, trabalhado no Google e Microsoft e ter ajudado a construir uma empresa, a Lemon no Vale do Silício. Brilhante né?! Seria, se o trabalho no Google e na Microsoft não fossem um estágio de 3 meses de verão, se ela fosse co-founder da empresa citada ou alguma coisa mais efetiva por lá.
Eu conheço muita gente nessa vida, meu DataEu é bem sofisticado, gente de todo canto, de diversas áreas, rico, pobre, gente que passou por variadas situações e tem muita divergência de opinião e visão de mundo. Tem gente que trabalha (trabalha mesmo) no Google, pra Amazon, startups brasileiras incríveis, empreendedores que são reis no Vale do Silício, que estudam ou estudaram no MIT, Harvard, Stanford, Oxford, Erasmus de Rotterdam (considerada a melhor escola de empreendedorismo do mundo), gente que representa o governo francês na União Européia, diretor de multinacional, vice-presidente de multinacional, milionário, multimilionário — infelizmente não conheço nenhum bilionário -, etc. O que quero dizer com isso?
Conheço no mínimo umas 50 pessoas 10 vezes mais importante e com história que realmente vale a pena ser explorada, mas não são, ou por opção, ou por falta de oportunidade.
Quando eu conheci a Bel Pesce, eu realmente fiquei empolgada para ouvir o que ela tinha para falar. Eu amo gente foda, gente que fez coisas que nunca fiz, que consegue cativar e ser reconhecida, enfim, eu gosto de gente brilhante.
Li o livro dela, achei bacana, bem escrito, nada glorioso, primoroso ou fora de série, mas atende bem a proposta. Comecei a ver os vídeos, a segui-la no twitter, a acompanhar no Periscope e foi ali, bem no meio daquela vontade de consumir um mundo do qual não tive a oportunidade de conhecer, que tive uma frustração bem grande.
O conhecimento que ela passava era tão profundo quanto um discurso da Dilma, mais raso que o nível que chegou a Cantareira. Algo como: “Essa empresa é top, é show, o que eles fazem é muito 10!”, “Empreender só depende de você”, “vá atrás dos seus sonhos”, “faça meta do dia”, sobre o negócio dela: “um negócio disruptivo, inovador, disuptamente novo”. Foi ali que fui atrás para entender quem era e porque ela tinha se tornado quem era. Essa conta não fechava. Deixei pra lá, não sou obrigada a consumir o que não quero e quem quiser que consuma. Ponto final!
Segui a vida… até que no início desse ano fiz um post questionando os “empreendedores motivacionais”, porque de repente eles se multiplicaram na internet. Eu não aguentava mais meta do dia, frases motivacionais, usei a expressão “essa geração Bel Pesce é legal mas a gente precisa mais no nosso dia a dia”. A crítica não era a ela, mas ao modelo replicado exaustivamente por diversas outras pessoas que se inspiraram nela.


Foi uma muvuca só. Aparentemente as pessoas tinham muito para falar sobre isso.
Conheci muita gente incrível por causa disso, inclusive uma das pessoas que me ajudaram a estruturar o atual projeto que estou trabalhando. Até brinquei que se desse certo, eu faria um post “Como a Bel Pesce me ajudou a ganhar meus primeiros milhões”.
Eu fui chamada de invejosa, diversas vezes, e coisa pior. Vieram dizer que a conheciam, que ela é um doce, e que era muito feio falar publicamente de uma pessoa. — ? Mesmo essa pessoa sendo uma pessoa pública?! Ué?! — O Murilo Gun, outra pessoa questionável, me chamou de “Bruna alguma coisa” em seu podcast e assim por diante.
Foi nesse momento que percebi que a Menina do Vale tinha virado, graças a ela mesma e sua constante autopromoção, um mito. E como todo famoso fruto da internet, de suas legiões incontáveis de fanáticos seguidores, é praticamente impossível questionar sem que os fãs da pessoa venham argumentar que você esteja criticando porque está com inveja.


A Bel vende e sempre vendeu o produto que ela construiu chamado “Bel Pesce”, todas as suas empresas são para fomentar esse mesmo produto. E ela faz isso de forma magistral.
Há mérito nesse imbróglio todo, nunca foi isso a ser questionado, o ponto que muita gente sempre levantou e que nos próximos meses ainda vão levantar é como uma pessoa pode se vender como suprassumo do empreendedorismo e inovação se o grande feito dela seja apenas e justamente ter feito sucesso por ensinar outras pessoas a empreenderem, e só.
É o mesmo que eu vender cursos caríssimos para ensinar outras pessoas a ficarem ricas, contando que fiquei rica, ensinando outras pessoas a ficarem rica e esse ciclo não tem fim.
E vou além, por que cargas d’água a gente escolhe líderes médios que tentam vender ilusões, fazem desserviço ao empreendedorismo dizendo que são e acontecem e que empreender só depende de você, cobrando e cobrando caro por cursos, palestras, chaveiro, hamburguer e passeio no Peru?
Enquanto a maioria dos empreendedores brasileiros abrem hamburgueria com R$15 mil reais num trailer com o dinheiro que passaram os últimos 65 anos juntando.
Se o problema for falta de referência, posso fazer uma lista de dezenas de pessoas realmente interessantes de serem admiradas por empreender honestamente e inovar disruptamente (existem grandes projetos no Brasil inteiro, principalmente no Norte e Nordeste).
Agora, não sei se a Bel aprendeu essa lição. Mas aprendemos, todos juntos, que estudar no MIT e estagiar no Google não ensina a abrir hamburgueria através de financiamento coletivo.
"""

tt = TextTeaser()
sentences = tt.summarize(title, text, count=10)
print(title)
for sentence in sentences:
  print(sentence)

