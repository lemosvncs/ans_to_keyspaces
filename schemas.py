# type(ambulatorialDet)
ambulatorialDet=dict({
        'allColumns': [
            {
                'name': 'ID_EVENTO_ATENCAO_SAUDE',
                'type': 'bigint'
            },
            {
                'name': 'UF_PRESTADOR',
                'type': 'text'
            },
            {
                'name': 'DT_REALIZACAO',
                'type': 'text'
            },
            {
                'name': 'CD_PROCEDIMENTO',
                'type': 'text'
            },
            {
                'name': 'CD_TABELA_REFERENCIA',
                'type': 'int'
            },
            {
                'name': 'QT_ITEM_EVENTO_INFORMADO',
                'type': 'int'
            },
            {
                'name': 'VL_ITEM_EVENTO_INFORMADO',
                'type': 'text'
            },
            {
                'name': 'VL_ITEM_PAGO_FORNECEDOR',
                'type': 'text'
            },
            {
                'name': 'IND_PACOTE',
                'type': 'int'
            },
            {
                'name': 'IND_TABELA_PROPRIA',
                'type': 'int'
            },
        ],
        'partitionKeys': [
            {
                'name': 'ID_EVENTO_ATENCAO_SAUDE'
            },
        ],
        # 'clusteringKeys': [
        #     {
        #         'name': 'string',
        #         'orderBy': 'ASC'|'DESC'
        #     },
        # ],
        # 'staticColumns': [
        #     {
        #         'name': 'string'
        #     },
        # ]
    })