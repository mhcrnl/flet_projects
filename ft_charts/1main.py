import flet as ft

def main(page: ft.Page):
    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(x=0, bar_rods=[ft.BarChartRod(from_y=0, to_y=40, color=ft.Colors.BLUE)]),
            ft.BarChartGroup(x=1, bar_rods=[ft.BarChartRod(from_y=0, to_y=100, color=ft.Colors.RED)]),
            ft.BarChartGroup(x=2, bar_rods=[ft.BarChartRod(from_y=0, to_y=30, color=ft.Colors.GREEN)]),
        ],
        border=ft.border.all(1, ft.Colors.GREY_400),
        left_axis=ft.ChartAxis(labels_size=40, title=ft.Text("Value")),
        bottom_axis=ft.ChartAxis(labels_size=40, title=ft.Text("Category")),
    )
    page.add(chart)

ft.app(target=main)
