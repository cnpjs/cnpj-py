import os

import pytest
import requests_mock

from cnpj import CNPJClient, CNPJError


def test_cnpj_client():
    json_mock = {
        "capital_social": 3403457800.0,
        "cnae_fiscal_principal": {
            "codigo": 5310501,
            "nome": "Atividades do Correio Nacional",
        },
        "cnae_fiscal_secundaria": [
            {"codigo": 5212500, "nome": "Carga e descarga"},
            {"codigo": 5232000, "nome": "Atividades de agenciamento marítimo"},
        ],
        "cnpj": "34028316000103",
        "data_inicio_atividade": "1970-02-13",
        "data_situacao_cadastral": "2005-11-03",
        "data_situacao_especial": None,
        "email": "ACGTESCNPJ@CORREIOS.COM.BR",
        "endereco": {
            "bairro": "ASA NORTE",
            "cep": "70002900",
            "complemento": "",
            "logradouro": "SBN QUADRA 1 BLOCO A",
            "municipio": "BRASILIA",
            "numero": "S/N",
            "tipo_logradouro": "SETOR",
            "uf": "DF",
        },
        "ente_federativo_responsavel": None,
        "motivo_situacao_cadastral": "SEM MOTIVO",
        "natureza_juridica": "Empresa Pública",
        "nome_da_cidade_no_exterior": None,
        "nome_fantasia": "CORREIOS SEDE",
        "pais": None,
        "porte": "",
        "qualificacao_responsavel": "Presidente",
        "razao_social": "EMPRESA BRASILEIRA DE CORREIOS E TELEGRAFOS",
        "situacao_cadastral": "Ativa",
        "situacao_especial": None,
        "socios": [
            {
                "data_entrada": "2021-11-25",
                "doc": "***425301**",
                "faixa_etaria": "41 a 50 anos",
                "nome": "HEGLEHYSCHYNTON VALERIO MARCAL",
                "pais": "",
                "qualificacao": "Diretor",
                "representante_legal": {
                    "doc": "***000000**",
                    "nome": "",
                    "qualificacao": "Não informada",
                },
                "tipo": "Pessoa física",
            },
        ],
        "telefone1": "6132144316",
        "telefone2": "00",
        "telefone_fax": "00",
    }

    with requests_mock.Mocker() as m:
        m.get("https://api.cnpjs.dev/v1/34028316000103", json=json_mock)
        cnpj_client = CNPJClient()
        result = cnpj_client.cnpj("34028316000103")
        assert result == json_mock


def test_get_cnpj_raises():
    with requests_mock.Mocker() as m:
        m.get("https://api.cnpjs.dev/v1/34028316000103", status_code=500)
        cnpj_client = CNPJClient()
        with pytest.raises(CNPJError):
            cnpj_client.cnpj("34028316000103")


@pytest.mark.skipif(
    os.getenv("CI_INTEGRATION") != "true",
    reason="CI_INTEGRATION environment variable != true",
)
def test_get_cnpj_integration():
    cnpj_client = CNPJClient()
    result = cnpj_client.cnpj("34028316000103")
    assert result != {}
