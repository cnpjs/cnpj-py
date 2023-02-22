# cnpj-py

Biblioteca Python para consulta de CNPJ (Cadastro Nacional de Pessoa Júridica)
usando a API do [cnpjs.dev](https://cnpjs.dev).

## Exemplo de uso

Essa bilbioteca expõe uma classe chmada `CNPJClient` com um único método `cnpj` que
recebe uma string contendo o CNPJ e retorna um dicionário com informações da
empresa registrada nesse CNPJ.

```python
from cnpj import CNPJClient
from pprint import pprint

cnpj_client = CNPJClient()
resultado = cnpj_client.cnpj('34028316000103')

pprint(resultado)
```

Saída do exemplo acima:

```python
{'capital_social': 3403457800.0,
 'cnae_fiscal_principal': {'codigo': 5310501,
                           'nome': 'Atividades do Correio Nacional'},
 'cnae_fiscal_secundaria': [{'codigo': 4713002,
                             'nome': 'Lojas de variedades, exceto lojas de '
                                     'departamentos ou magazines'},
                            {'codigo': 4761003,
                             'nome': 'Comércio varejista de artigos de '
                                     'papelaria'},
                            {'codigo': 4789099,
                             'nome': 'Comércio varejista de outros produtos '
                                     'não especificados anteriormente'},
                            {'codigo': 5211701,
                             'nome': 'Armazéns gerais - emissão de warrant'},
                            {'codigo': 5211799,
                             'nome': 'Depósitos de mercadorias para terceiros, '
                                     'exceto armazéns gerais e guarda-móveis'},
                            {'codigo': 5212500, 'nome': 'Carga e descarga'},
                            {'codigo': 5232000,
                             'nome': 'Atividades de agenciamento marítimo'},
                            {'codigo': 5250801,
                             'nome': 'Comissaria de despachos'},
                            {'codigo': 5250803,
                             'nome': 'Agenciamento de cargas, exceto para o '
                                     'transporte marítimo'},
                            {'codigo': 5250805,
                             'nome': 'Operador de transporte multimodal - OTM'},
                            {'codigo': 6619302,
                             'nome': 'Correspondentes de instituições '
                                     'financeiras'},
                            {'codigo': 6619399,
                             'nome': 'Outras atividades auxiliares dos '
                                     'serviços financeiros não especificadas '
                                     'anteriormente'},
                            {'codigo': 7740300,
                             'nome': 'Gestão de ativos intangíveis '
                                     'não-financeiros'},
                            {'codigo': 8219901, 'nome': 'Fotocópias'},
                            {'codigo': 8219999,
                             'nome': 'Preparação de documentos e serviços '
                                     'especializados de apoio administrativo '
                                     'não especificados anteriormente'}],
 'cnpj': '34028316000103',
 'data_inicio_atividade': '1970-02-13',
 'data_situacao_cadastral': '2005-11-03',
 'data_situacao_especial': None,
 'email': 'ACGTESCNPJ@CORREIOS.COM.BR',
 'endereco': {'bairro': 'ASA NORTE',
              'cep': '70002900',
              'complemento': '',
              'logradouro': 'SBN QUADRA 1 BLOCO A',
              'municipio': 'BRASILIA',
              'numero': 'S/N',
              'tipo_logradouro': 'SETOR',
              'uf': 'DF'},
 'ente_federativo_responsavel': None,
 'motivo_situacao_cadastral': 'SEM MOTIVO',
 'natureza_juridica': 'Empresa Pública',
 'nome_da_cidade_no_exterior': None,
 'nome_fantasia': 'CORREIOS SEDE',
 'pais': None,
 'porte': '',
 'qualificacao_responsavel': 'Presidente',
 'razao_social': 'EMPRESA BRASILEIRA DE CORREIOS E TELEGRAFOS',
 'situacao_cadastral': 'Ativa',
 'situacao_especial': None,
 'socios': [{'data_entrada': '2021-11-25',
             'doc': '***425301**',
             'faixa_etaria': '41 a 50 anos',
             'nome': 'HEGLEHYSCHYNTON VALERIO MARCAL',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2019-11-20',
             'doc': '***781871**',
             'faixa_etaria': '51 a 60 anos',
             'nome': 'CARLOS HENRIQUE DE LUCA OLIVEIRA RIBEIRO',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2022-08-22',
             'doc': '***580075**',
             'faixa_etaria': '41 a 50 anos',
             'nome': 'MERCIA DA SILVA PEDREIRA',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2019-07-22',
             'doc': '***228101**',
             'faixa_etaria': '41 a 50 anos',
             'nome': 'ALEX DO NASCIMENTO',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2019-08-21',
             'doc': '***902306**',
             'faixa_etaria': '61 a 70 anos',
             'nome': 'FLORIANO PEIXOTO VIEIRA NETO',
             'pais': '',
             'qualificacao': 'Presidente',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2021-12-01',
             'doc': '***235807**',
             'faixa_etaria': '51 a 60 anos',
             'nome': 'JOSE EDUARDO LEAL DE OLIVEIRA',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'},
            {'data_entrada': '2019-11-21',
             'doc': '***135107**',
             'faixa_etaria': '51 a 60 anos',
             'nome': 'DANILO CEZAR AGUIAR DE SOUZA',
             'pais': '',
             'qualificacao': 'Diretor',
             'representante_legal': {'doc': '***000000**',
                                     'nome': '',
                                     'qualificacao': 'Não informada'},
             'tipo': 'Pessoa física'}],
 'telefone1': '6132144316',
 'telefone2': '00',
 'telefone_fax': '00'}
```

## Documentação do endpoint HTTP

Consulte a documentação completa da API em [https://cnpjs.dev/docs](https://cnpjs.dev/docs).

## Limites de uso

Qualquer tentativa de abuso da API poderá ocasionar o bloqueio do acesso ou um
limite do número de requisições por segundo. O objetivo dessas limitações é
garantir a disponibilidade e a estabilidade da API para todos os usuários.

