import flet as ft

def simulator(page: ft.Page, width: int, height: int, conditions: dict):
    
    def inserting_conditions():
        condition_column.controls.clear()
        
        if len(conditions) > 0:
            for condition in conditions:
                condition_column.controls.append(
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=condition,
                                size=13,
                                color=ft.colors.WHITE,
                                weight='bold'
                            ),
                            ft.Text(
                                value=conditions[condition].upper() if type(conditions[condition]) == str else format(conditions[condition], ",.2f"),
                                size=13,
                                color=ft.colors.BLUE,
                                weight='bold'
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
        
            # inserindo as linhas na tabela
            montante = conditions['Montante de Financiamento']
            n = conditions['Prazo da Operação']
            p = conditions['Periodicidade']
            t = conditions['Diferimento']
            i = (conditions['Taxa de juro']/100)/(12/p)
            prestacao = (montante * i) / (1 - (1 + i)**(-(n/p) + t))
            
            tabela_amortizacao.rows.clear()
            for k in range(0, int(n/p) + 1):
                if k == 0:
                    tabela_amortizacao.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(value=k, size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(0, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(0, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(0, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                            ]
                        )
                    )
                
                elif k > 0 and k <= t:
                    juros = montante * i
                    tabela_amortizacao.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(value=k, size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(juros, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(0, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(juros, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                            ]
                        )
                    )
                
                elif k > 0 and k > t:
                    inicial = float(tabela_amortizacao.rows[-1].cells[-1].content.value.replace(',',''))
                    juros = inicial * i
                    capital = prestacao - juros
                    final = inicial - capital
                    
                    tabela_amortizacao.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(value=k, size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(inicial, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(juros, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(capital, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(prestacao, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                                ft.DataCell(content=ft.Text(value=format(final, ",.2f"), size=13, weight='bold', color=ft.colors.WHITE)),
                            ]
                        )
                    )
                
                if k == int(n/p):
                    total_prestacao = prestacao * (n/p)
                    total_juros = total_prestacao - montante
                    tabela_amortizacao.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(value='TOTAL'.upper(), size=14, weight='bold', color=ft.colors.BLUE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=14, weight='bold', color=ft.colors.BLUE)),
                                ft.DataCell(content=ft.Text(value=format(total_juros, ",.2f"), size=14, weight='bold', color=ft.colors.BLUE)),
                                ft.DataCell(content=ft.Text(value=format(montante, ",.2f"), size=14, weight='bold', color=ft.colors.BLUE)),
                                ft.DataCell(content=ft.Text(value=format(total_prestacao, ",.2f"), size=14, weight='bold', color=ft.colors.BLUE)),
                                ft.DataCell(content=ft.Text(value=format(0, ",.2f"), size=14, weight='bold', color=ft.colors.BLUE)),
                            ]
                        )
                    )
    
    # criando a view simulator
    view = ft.View(
        route='/simulator',
        controls=[
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={'md': 3},
                        height=height * 0.90,
                        border_radius=10,
                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                        padding=ft.padding.only(
                            left=10,
                            right=10,
                            top=8
                        ),
                        
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value='Condições de Financiamento'.upper(),
                                    size=16,
                                    weight='bold',
                                    color=ft.colors.WHITE
                                ),
                                ft.Divider(
                                    height=1,
                                    color=ft.colors.WHITE,
                                    visible=True
                                ),
                                
                                condition_column := ft.Column(
                                    controls=[
                                        
                                    ]
                                )
                            ]
                        )
                    ),
                    
                    ft.Container(
                        col={'sm': 12, 'md': 9},
                        height=height * 0.90,
                        border_radius=10,
                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLUE),
                        padding=ft.padding.only(
                            left=10,
                            right=10,
                            top=8
                        ),
                        
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value='Tabela de Amortização'.upper(),
                                    size=16,
                                    weight='bold',
                                    color=ft.colors.WHITE
                                ),
                                ft.Divider(
                                    height=1,
                                    color=ft.colors.WHITE,
                                    visible=True
                                ),
                                
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                tabela_amortizacao := ft.DataTable(
                                                    show_bottom_border=True,
                                                    
                                                    columns=[
                                                        ft.DataColumn(label=ft.Text(value='Nº', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                        ft.DataColumn(label=ft.Text(value='Inicial', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                        ft.DataColumn(label=ft.Text(value='Juros', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                        ft.DataColumn(label=ft.Text(value='Capital', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                        ft.DataColumn(label=ft.Text(value='Prestação', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                        ft.DataColumn(label=ft.Text(value='Final', size=13, weight='bold', color=ft.colors.WHITE), numeric=True),
                                                    ],
                                                    rows=[
                                                        
                                                    ],
                                                    width=width * 0.72,
                                                    heading_row_height=35
                                                )
                                            ],
                                            height=height * 0.82,
                                            scroll=ft.ScrollMode.AUTO
                                        )
                                    ],
                                    scroll=ft.ScrollMode.AUTO
                                )
                            ]
                        )
                    )
                ],
                spacing=3
            )
        ],
        appbar=ft.AppBar(
            actions=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.HOME,
                            icon_size=25,
                            icon_color=ft.colors.with_opacity(0.5, ft.colors.with_opacity),
                            on_click= lambda e: page.go('/')
                        ),
                        ft.IconButton(
                            icon=ft.icons.LOGOUT,
                            icon_size=25,
                            icon_color=ft.colors.with_opacity(0.5, ft.colors.with_opacity),
                            on_click= lambda e: page.go('/')
                        )
                    ]
                )
            ],
            bgcolor=ft.colors.BLUE,
            toolbar_height=40
        )
    )
    
    inserting_conditions()
    page.update()
    
    return view