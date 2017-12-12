# coletivo-rexiste
Aplicação Django para o site do Coletivo Rexiste

---

Este é o programa que permite funcionar o site do coletivo Rexiste. Ainda est em processo de desenvolvimento e de forma alguma esta é a versão final, principalmente no que tange aspectos de design gráfico.

O programa é escrito com apoio da framework Django, em Python. É usada a framework CSS/JS Bootstrap 3. 

Há um pequeno script adicional em jQuery.

Tambem foram adicionados as aplicaçoes "hitcount" e a versão community do editor HTML "CKEditor".

---

Embora esta seja a primeira versão disponvel no repositório, ela não é a primeira versão de todas. A primeira havia algumas pequenas falhas, que foram corrigidas nesta versão. A primeira versão não há de ser encontrada no histórico pois eu precisei deletá-la, já que, sem querer, acabei fazendo o upload the informação confidencial que jazia em settings.py (senha do email, senha secreta do app, email secreto.), e fiz uso do git filter-branch de modo que, acredito eu, acidentalmente gerou alguns bugs no meu repositório original, mas estes já foram corrigidos neste.

À esta verso, de diferente da outra, foi adicionado o seguinte: 

* as páginas de erro (400, 403, 404, 500);
* os links para nossas redes sociais (Twitter, Facebook e Instagram);
* foi ajustado o footer para que não sumisse no mobile
* foi alterado parte do design da página principal (em vez de três thumbnails agora são quatro; em vez de "Sobre Nós", "Contato" e "Contribua" agora se mostra a configuração atual, que não inclui mais "Contribua", e inclui "Informe-se".
* Foram limpados alguns arquivos que se mostravam inúteis e não estavam sob uso (o famoso "código comentado").
