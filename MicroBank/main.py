import flet as ft
from views.home import home, conditions
from views.error404 import error404
from views.simulator import simulator

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = page.route
    
    WIDTH = page.width
    HEIGHT = page.height
    
    def route_change(route: str):
        page.views.clear()
        
        for control in page.overlay:
            if control._get_control_name() == 'alertdialog':
                control.open = False
                page.update()
        
        if page.route == '/':
            page.views.append(home(page, WIDTH, HEIGHT))
        
        elif page.route == '/simulator':
            page.views.append(simulator(page, WIDTH, HEIGHT, conditions))
        
        else:
            page.views.append(error404(page, WIDTH, HEIGHT))
        
        page.title = page.route
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

if __name__ == '__main__':
    app = ft.app(target=main, view=ft.WEB_BROWSER)