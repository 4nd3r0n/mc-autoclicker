from flet import (
    app, Page, ControlEvent,
    MainAxisAlignment, CrossAxisAlignment,
    Container, AppBar,
    ElevatedButton,
    Colors, Icons,
)
from service.autoclick import AutoClick
auto_click=AutoClick()

def config(page: Page) -> None:
    page.title="AutoClicker Minecraft"
    page.bgcolor=Colors.GREEN_200
    page.horizontal_alignment=CrossAxisAlignment.CENTER
    page.vertical_alignment=MainAxisAlignment.CENTER
    page.window.resizable=False
    page.window.height=200
    page.window.width=200

class AutoClicker(Container):
    def __init__(self) -> None:
        super().__init__()
        self.start_stop=ElevatedButton(
            text="Start",
            on_click=lambda e: self.click_start(e),
        )
        self.content=self.start_stop

    def click_start(self, e: ControlEvent) -> None:
        match e.control.text:
            case "Start":
                self.start_stop.text="Stop"
                e.page.update()
                auto_click.start()
            case "Stop":
                self.start_stop.text="Start"
                e.page.update()
                auto_click.stop()

def main(page: Page) -> None:
    config(page)
    page.add(
        AutoClicker(),
    )

app(main)
