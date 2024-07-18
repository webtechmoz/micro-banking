import flet as ft

def error404(page: ft.Page, width: int, height: int):
    
    view = ft.View(
        route='/',
        controls=[
            ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.WIFI_OFF,
                        size=25,
                        color=ft.colors.RED
                    ),
                    
                    ft.Text(
                        value="Oop's, esta página não existe".upper(),
                        size=16,
                        color=ft.colors.WHITE,
                        weight='bold'
                    ),
                    
                    ft.IconButton(
                        icon=ft.icons.ARROW_RIGHT,
                        icon_size=25,
                        icon_color=ft.colors.WHITE,
                        on_click= lambda e: page.go('/')
                    )
                ],
                height=height,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )
    return view