import flet as ft

def SnackBar(page: ft.Page, icon: ft.icons, value: str, color: ft.colors, bgcolor: ft.colors = None):
    
    snackbar = ft.SnackBar(
        bgcolor=bgcolor,
        content=ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=25,
                    color=color
                ),
                
                ft.Text(
                    value=value,
                    color=color,
                    size=13,
                    weight='bold'
                )
            ]
        )
    )
    
    page.overlay.append(snackbar)
    snackbar.open = True
    page.update()
    
    return snackbar

def clicked(page: ft.Page, e: ft.ControlEvent):
    
    SnackBar(icon=ft.icons.MENU_BOOK, value=e.control, color=ft.colors.BLUE)
    
    page.update()

def TextField(hint_text: str, prefix_icon: ft.icons, color: ft.colors, size: int, bgcolor: ft.colors,width: int = None, height: int = None, col: dict = None):
    
    textfield = ft.TextField(
        hint_text=hint_text,
        hint_style=ft.TextStyle(
            color=ft.colors.with_opacity(0.2, color),
            size=size,
            weight='bold'
        ),
        prefix_icon=prefix_icon,
        prefix_style=ft.TextStyle(
            color=ft.colors.with_opacity(0.2, color),
            size=18,
            weight='bold'
        ),
        text_style=ft.TextStyle(
            color=color,
            size=size,
            weight='bold'
        ),
        border=ft.InputBorder.UNDERLINE,
        border_radius=10,
        border_width=0.5,
        border_color=ft.colors.with_opacity(0.1, bgcolor),
        bgcolor=ft.colors.with_opacity(0.1, bgcolor),
        text_vertical_align=-0.4,
        col=col,
        width=width,
        height=height
    )
    
    return textfield