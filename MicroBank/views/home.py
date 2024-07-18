import flet as ft
import sys

sys.path.append('utils')
from  utils.controls import TextField, SnackBar, clicked
conditions = {}

def home(page: ft.Page, width: int, height: int):
    
    view = ft.View(
        route='/',
        controls=[
            ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.WALLET,
                        size=25,
                        color=ft.colors.BLUE
                    ),
                    
                    ft.Text(
                        value='Micro Banking'.upper(),
                        size=16,
                        color=ft.colors.WHITE,
                        weight='bold'
                    ),
                    
                    ft.IconButton(
                        icon=ft.icons.ARROW_RIGHT,
                        icon_size=25,
                        icon_color=ft.colors.WHITE,
                        on_click= lambda e: _AlertDialog(page, height)
                    )
                ],
                height=height,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )
    return view

def _AlertDialog(page: ft.Page, height: int):
    
    controls = {
        'Nome do Proponente': ft.icons.PERSON,
        'Tipo de Garantia': ft.icons.HOME,
        'Valor da Garantia': ft.icons.MONEY,
        'Taxa de juro': ft.icons.PERCENT,
        'Montante de Financiamento': ft.icons.MONETIZATION_ON,
        'Prazo da Operação': ft.icons.DATE_RANGE,
        'Periodicidade': ft.icons.DATA_ARRAY,
        'Diferimento': ft.icons.DIFFERENCE
    }
    
    float_controls = ['Valor da Garantia', 'Taxa de juro', 'Montante de Financiamento', 'Prazo da Operação', 'Periodicidade', 'Diferimento']
    
    def close(e):
        alertdialog.open = False
        page.update()
    
    def go_simulator(e):
        global conditions
        
        preenchido = False
        for i, control in enumerate(condition_controls.controls):
            if control.controls[1].value == '':
                SnackBar(page, ft.icons.CLOSE, f'O campo *{control.controls[1].hint_text}* precisa ser preenchido', ft.colors.RED)
                conditions.clear()
                break
            
            else:
                if control.controls[1].hint_text in float_controls:
                    try:
                        conditions.setdefault(control.controls[1].hint_text,float(control.controls[1].value))
                        
                    except:
                        SnackBar(page, ft.icons.CLOSE, f'O campo *{control.controls[1].hint_text}* deve ser numérico', ft.colors.RED)
                        conditions.clear()
                        break
                
                else:
                    conditions.setdefault(control.controls[1].hint_text,control.controls[1].value)
            
            if i == len(condition_controls.controls) - 1:
                preenchido = True

        if preenchido == True:
            vg = conditions[float_controls[0]]
            i = conditions[float_controls[1]]
            montante = conditions[float_controls[2]]
            n = conditions[float_controls[3]]
            p = conditions[float_controls[4]]
            t = conditions[float_controls[5]]
            
            if montante > vg:
                SnackBar(page, ft.icons.CLOSE, f'O financiamento não pode ser maior que a garantia', ft.colors.RED)
                conditions.clear()
            
            elif montante <= vg and i >= 0 and t >=0 and n % p == 0 and (n/p) > t:
                page.go('/simulator')
                page.update()
            
            else:
                SnackBar(page, ft.icons.CLOSE, f'Verifique a taxa de juro, o prazo, a periodicidade e o diferimento', ft.colors.RED)
                conditions.clear()
    
    alertdialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            controls=[
                ft.Text(
                    value='Condições de Financiamento',
                    color=ft.colors.WHITE,
                    weight='bold',
                    size=18
                ),
                
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_size=25,
                    icon_color=ft.colors.RED,
                    on_click=close
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        content=ft.Column(
            controls=[
                ft.Divider(
                    height=1,
                    visible=True,
                    color=ft.colors.WHITE
                ),
                condition_controls := ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Text(
                                    value=control,
                                    size=13,
                                    color=ft.colors.WHITE,
                                    weight='bold',
                                    col={'sm': 12}
                                ),
                                
                                TextField(
                                    hint_text=control,
                                    prefix_icon=controls[control],
                                    color=ft.colors.WHITE,
                                    size=13,
                                    bgcolor=ft.colors.BLACK,
                                    col={'sm': 12}
                                )
                            ]
                        ) for control in controls
                    ]
                )
            ],
            height=height * 0.67,
            scroll=ft.ScrollMode.AUTO
        ),
        actions=[
            ft.ResponsiveRow(
                controls=[
                    ft.FloatingActionButton(
                        text='Simulator',
                        bgcolor=ft.colors.BLUE,
                        foreground_color=ft.colors.WHITE,
                        on_click= go_simulator,
                        col={'sm': 12},
                        height=40
                    )
                ]
            )
        ]
    )
    
    page.overlay.append(alertdialog)
    alertdialog.open = True
    page.update()
    
    return alertdialog