import json


class MockDao:

    # 模拟城市视野绿线服务
    def get_city(self):
        body = {
            "features": [
                {
                    "geometry": {
                        "coordinates": [
                            [
                                [
                                    [
                                        123.29848962672438,
                                        41.844326160308924
                                    ],
                                    [
                                        123.2948028122347,
                                        41.84450822785801
                                    ]
                                ]
                            ],
                            [
                                [
                                    [
                                        123.51933628371017,
                                        41.89049535535285
                                    ],
                                    [
                                        123.5203070616039,
                                        41.88960818239942
                                    ]
                                ]
                            ]
                        ],
                        "type": "MultiPolygon"
                    },
                    "id": "1",
                    "type": "Feature",
                    "properties": {}
                }
            ],
            "type": "FeatureCollection"
        }
        return body

    def get_guangzhou(self):
        body = {
            "features": [
                {
                    "geometry": {
                        "coordinates": [
                            [
                                [
                                    [
                                        123.29848962672438,
                                        41.844326160308924
                                    ],
                                    [
                                        123.2948028122347,
                                        41.84450822785801
                                    ]
                                ]
                            ],
                            [
                                [
                                    [
                                        123.51933628371017,
                                        41.89049535535285
                                    ],
                                    [
                                        123.5203070616039,
                                        41.88960818239942
                                    ]
                                ]
                            ]
                        ],
                        "type": "MultiPolygon"
                    },
                    "id": "1",
                    "type": "Feature",
                    "properties": {}
                }
            ],
            "type": "FeatureCollection"
        }
        return body
