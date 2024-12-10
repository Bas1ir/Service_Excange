from typing import Any, Type

from matplotlib._api import classproperty
from matplotlib.backend_bases import (
    FigureCanvasBase,
    FigureManagerBase,
    MouseButton,
    NavigationToolbar2,
    TimerBase,
    ToolContainerBase,
    _Backend,
)
from matplotlib.transforms import Bbox

from .. import backend_tools
from .qt_compat import QtCore, QtWidgets

backend_version = ...
SPECIAL_KEYS: dict = ...

cursord: dict[backend_tools.Cursors, Any] = ...

class __getattr__:
    qApp = ...

class TimerQT(TimerBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __del__(self) -> None: ...

class FigureCanvasQT(QtWidgets.QWidget, FigureCanvasBase):
    required_interactive_framework: str = ...
    _timer_cls: Type[TimerQT] = TimerQT
    manager_class: classproperty = ...
    buttond: dict[str, MouseButton] = ...

    def __init__(self, figure=...) -> None: ...
    def showEvent(self, event) -> None: ...
    def set_cursor(self, cursor: backend_tools.Cursors) -> None: ...
    def enterEvent(self, event) -> None: ...
    def leaveEvent(self, event) -> None: ...
    def mouseEventCoords(self, pos) -> tuple[float, float]: ...
    def mousePressEvent(self, event) -> None: ...
    def mouseDoubleClickEvent(self, event) -> None: ...
    def mouseMoveEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    def wheelEvent(self, event) -> None: ...
    def keyPressEvent(self, event) -> None: ...
    def keyReleaseEvent(self, event) -> None: ...
    def resizeEvent(self, event) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def minumumSizeHint(self) -> QtCore.QSize: ...
    def flush_events(self) -> None: ...
    def start_event_loop(self, timeout=...) -> None: ...
    def stop_event_loop(self, event=...) -> None: ...
    def draw(self) -> None: ...
    def draw_idle(self) -> None: ...
    def blit(self, bbox: Bbox | None = None) -> None: ...
    def drawRectangle(self, rect) -> None: ...

class MainWindow(QtWidgets.QMainWindow):
    closing: QtCore.Signal = ...
    def closeEvent(self, event) -> None: ...

class FigureManagerQT(FigureManagerBase):
    def __init__(self, canvas: FigureCanvasBase, num: int | str) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def resize(self, width, height) -> None: ...
    def show(self) -> None: ...
    def destroy(self, *args) -> None: ...
    def get_window_title(self) -> None: ...
    def set_window_title(self, title) -> None: ...

class NavigationToolbar2QT(NavigationToolbar2, QtWidgets.QToolBar):
    message: QtCore.Signal = ...
    toolitems: list = ...
    def __init__(self, canvas, parent=..., coordinates=...) -> None: ...
    def edit_parameters(self) -> None: ...
    def pan(self, *args) -> None: ...
    def zoom(self, *args) -> None: ...
    def set_message(self, s) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    def configure_subplots(self) -> SubplotToolQt: ...
    def save_figure(self, *args) -> None: ...
    def set_history_buttons(self) -> None: ...

class SubplotToolQt(QtWidgets.QDialog):
    def __init__(self, targetfig, parent) -> None: ...
    def update_from_current_subplotpars(self) -> None: ...

class ToolbarQt(ToolContainerBase, QtWidgets.QToolBar):
    def __init__(self, toolmanager, parent=...) -> None: ...
    def add_toolitem(
        self,
        name: str,
        group: str,
        position: int,
        image_file,
        description: str,
        toggle: bool,
    ) -> None: ...
    def toggle_toolitem(self, name: str, toggled: bool) -> None: ...
    def remove_toolitem(self, name: str) -> None: ...
    def set_message(self, s: str) -> None: ...

class ConfigureSubplotsQt(backend_tools.ConfigureSubplotsBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def trigger(self, *args) -> None: ...

class SaveFigureQt(backend_tools.SaveFigureBase):
    def trigger(self, *args) -> None: ...

class SetCursorQt(backend_tools.SetCursorBase):
    def set_cursor(self, cursor) -> None: ...

class RubberbandQt(backend_tools.RubberbandBase):
    def draw_rubberband(self, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...

class HelpQt(backend_tools.ToolHelpBase):
    def trigger(self, *args) -> None: ...

class ToolCopyToClipboardQT(backend_tools.ToolCopyToClipboardBase):
    def trigger(self, *args, **kwargs) -> None: ...

class _BackendQT(_Backend):
    FigureCanvas = FigureCanvasQT
    FigureManager = FigureManagerQT
    @staticmethod
    def mainloop() -> None: ...
