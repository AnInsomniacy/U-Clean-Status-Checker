# The PEP 484 type hints stub file for the QtDesigner module.
#
# Generated by SIP 6.8.0
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtWidgets

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QDesignerActionEditorInterface(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget], flags: QtCore.Qt.WindowType = ...) -> None: ...

    def setFormWindow(self, formWindow: typing.Optional['QDesignerFormWindowInterface']) -> None: ...
    def unmanageAction(self, action: typing.Optional[QtGui.QAction]) -> None: ...
    def manageAction(self, action: typing.Optional[QtGui.QAction]) -> None: ...
    def core(self) -> typing.Optional['QDesignerFormEditorInterface']: ...


class QAbstractFormBuilder(PyQt6.sip.simplewrapper):

    def __init__(self) -> None: ...

    def errorString(self) -> str: ...
    def workingDirectory(self) -> QtCore.QDir: ...
    def setWorkingDirectory(self, directory: QtCore.QDir) -> None: ...
    def save(self, dev: typing.Optional[QtCore.QIODevice], widget: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def load(self, device: typing.Optional[QtCore.QIODevice], parent: typing.Optional[QtWidgets.QWidget] = ...) -> typing.Optional[QtWidgets.QWidget]: ...


class QDesignerFormEditorInterface(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setActionEditor(self, actionEditor: typing.Optional[QDesignerActionEditorInterface]) -> None: ...
    def setObjectInspector(self, objectInspector: typing.Optional['QDesignerObjectInspectorInterface']) -> None: ...
    def setPropertyEditor(self, propertyEditor: typing.Optional['QDesignerPropertyEditorInterface']) -> None: ...
    def setWidgetBox(self, widgetBox: typing.Optional['QDesignerWidgetBoxInterface']) -> None: ...
    def actionEditor(self) -> typing.Optional[QDesignerActionEditorInterface]: ...
    def formWindowManager(self) -> typing.Optional['QDesignerFormWindowManagerInterface']: ...
    def objectInspector(self) -> typing.Optional['QDesignerObjectInspectorInterface']: ...
    def propertyEditor(self) -> typing.Optional['QDesignerPropertyEditorInterface']: ...
    def widgetBox(self) -> typing.Optional['QDesignerWidgetBoxInterface']: ...
    def topLevel(self) -> typing.Optional[QtWidgets.QWidget]: ...
    def extensionManager(self) -> typing.Optional['QExtensionManager']: ...


class QDesignerFormWindowInterface(QtWidgets.QWidget):

    class FeatureFlag(enum.Flag):
        EditFeature = ... # type: QDesignerFormWindowInterface.FeatureFlag
        GridFeature = ... # type: QDesignerFormWindowInterface.FeatureFlag
        TabOrderFeature = ... # type: QDesignerFormWindowInterface.FeatureFlag
        DefaultFeature = ... # type: QDesignerFormWindowInterface.FeatureFlag

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...

    def activateResourceFilePaths(self, paths: typing.Iterable[typing.Optional[str]]) -> typing.Tuple[typing.Optional[int], typing.Optional[str]]: ...
    def formContainer(self) -> typing.Optional[QtWidgets.QWidget]: ...
    def activeResourceFilePaths(self) -> typing.List[str]: ...
    def checkContents(self) -> typing.List[str]: ...
    objectRemoved: typing.ClassVar[QtCore.pyqtSignal]
    widgetRemoved: typing.ClassVar[QtCore.pyqtSignal]
    changed: typing.ClassVar[QtCore.pyqtSignal]
    activated: typing.ClassVar[QtCore.pyqtSignal]
    aboutToUnmanageWidget: typing.ClassVar[QtCore.pyqtSignal]
    widgetUnmanaged: typing.ClassVar[QtCore.pyqtSignal]
    widgetManaged: typing.ClassVar[QtCore.pyqtSignal]
    resourceFilesChanged: typing.ClassVar[QtCore.pyqtSignal]
    geometryChanged: typing.ClassVar[QtCore.pyqtSignal]
    selectionChanged: typing.ClassVar[QtCore.pyqtSignal]
    featureChanged: typing.ClassVar[QtCore.pyqtSignal]
    fileNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    mainContainerChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setFileName(self, fileName: typing.Optional[str]) -> None: ...
    def setGrid(self, grid: QtCore.QPoint) -> None: ...
    def selectWidget(self, widget: typing.Optional[QtWidgets.QWidget], select: bool = ...) -> None: ...
    def clearSelection(self, update: bool = ...) -> None: ...
    def setDirty(self, dirty: bool) -> None: ...
    def setFeatures(self, f: 'QDesignerFormWindowInterface.FeatureFlag') -> None: ...
    def unmanageWidget(self, widget: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def manageWidget(self, widget: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def removeResourceFile(self, path: typing.Optional[str]) -> None: ...
    def addResourceFile(self, path: typing.Optional[str]) -> None: ...
    def resourceFiles(self) -> typing.List[str]: ...
    def emitSelectionChanged(self) -> None: ...
    @typing.overload
    @staticmethod
    def findFormWindow(w: typing.Optional[QtWidgets.QWidget]) -> typing.Optional['QDesignerFormWindowInterface']: ...
    @typing.overload
    @staticmethod
    def findFormWindow(obj: typing.Optional[QtCore.QObject]) -> typing.Optional['QDesignerFormWindowInterface']: ...
    def isDirty(self) -> bool: ...
    def isManaged(self, widget: typing.Optional[QtWidgets.QWidget]) -> bool: ...
    def setMainContainer(self, mainContainer: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def mainContainer(self) -> typing.Optional[QtWidgets.QWidget]: ...
    def grid(self) -> QtCore.QPoint: ...
    def cursor(self) -> typing.Optional['QDesignerFormWindowCursorInterface']: ...
    def core(self) -> typing.Optional[QDesignerFormEditorInterface]: ...
    def setIncludeHints(self, includeHints: typing.Iterable[typing.Optional[str]]) -> None: ...
    def includeHints(self) -> typing.List[str]: ...
    def setExportMacro(self, exportMacro: typing.Optional[str]) -> None: ...
    def exportMacro(self) -> str: ...
    def setPixmapFunction(self, pixmapFunction: typing.Optional[str]) -> None: ...
    def pixmapFunction(self) -> str: ...
    def setLayoutFunction(self, margin: typing.Optional[str], spacing: typing.Optional[str]) -> None: ...
    def layoutFunction(self) -> typing.Tuple[typing.Optional[str], typing.Optional[str]]: ...
    def setLayoutDefault(self, margin: int, spacing: int) -> None: ...
    def layoutDefault(self) -> typing.Tuple[typing.Optional[int], typing.Optional[int]]: ...
    def setComment(self, comment: typing.Optional[str]) -> None: ...
    def comment(self) -> str: ...
    def setAuthor(self, author: typing.Optional[str]) -> None: ...
    def author(self) -> str: ...
    def hasFeature(self, f: 'QDesignerFormWindowInterface.FeatureFlag') -> bool: ...
    def features(self) -> 'QDesignerFormWindowInterface.FeatureFlag': ...
    @typing.overload
    def setContents(self, dev: typing.Optional[QtCore.QIODevice], errorMessage: typing.Optional[typing.Optional[str]] = ...) -> bool: ...
    @typing.overload
    def setContents(self, contents: typing.Optional[str]) -> bool: ...
    def contents(self) -> str: ...
    def absoluteDir(self) -> QtCore.QDir: ...
    def fileName(self) -> str: ...


class QDesignerFormWindowCursorInterface(PyQt6.sip.simplewrapper):

    class MoveMode(enum.Enum):
        MoveAnchor = ... # type: QDesignerFormWindowCursorInterface.MoveMode
        KeepAnchor = ... # type: QDesignerFormWindowCursorInterface.MoveMode

    class MoveOperation(enum.Enum):
        NoMove = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Start = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        End = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Next = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Prev = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Left = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Right = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Up = ... # type: QDesignerFormWindowCursorInterface.MoveOperation
        Down = ... # type: QDesignerFormWindowCursorInterface.MoveOperation

    def __init__(self) -> None: ...

    def isWidgetSelected(self, widget: typing.Optional[QtWidgets.QWidget]) -> bool: ...
    def resetWidgetProperty(self, widget: typing.Optional[QtWidgets.QWidget], name: typing.Optional[str]) -> None: ...
    def setWidgetProperty(self, widget: typing.Optional[QtWidgets.QWidget], name: typing.Optional[str], value: typing.Any) -> None: ...
    def setProperty(self, name: typing.Optional[str], value: typing.Any) -> None: ...
    def selectedWidget(self, index: int) -> typing.Optional[QtWidgets.QWidget]: ...
    def selectedWidgetCount(self) -> int: ...
    def hasSelection(self) -> bool: ...
    def widget(self, index: int) -> typing.Optional[QtWidgets.QWidget]: ...
    def widgetCount(self) -> int: ...
    def current(self) -> typing.Optional[QtWidgets.QWidget]: ...
    def setPosition(self, pos: int, mode: 'QDesignerFormWindowCursorInterface.MoveMode' = ...) -> None: ...
    def position(self) -> int: ...
    def movePosition(self, op: 'QDesignerFormWindowCursorInterface.MoveOperation', mode: 'QDesignerFormWindowCursorInterface.MoveMode' = ...) -> bool: ...
    def formWindow(self) -> typing.Optional[QDesignerFormWindowInterface]: ...


class QDesignerFormWindowManagerInterface(QtCore.QObject):

    class ActionGroup(enum.Enum):
        StyledPreviewActionGroup = ... # type: QDesignerFormWindowManagerInterface.ActionGroup

    class Action(enum.Enum):
        CutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        CopyAction = ... # type: QDesignerFormWindowManagerInterface.Action
        PasteAction = ... # type: QDesignerFormWindowManagerInterface.Action
        DeleteAction = ... # type: QDesignerFormWindowManagerInterface.Action
        SelectAllAction = ... # type: QDesignerFormWindowManagerInterface.Action
        LowerAction = ... # type: QDesignerFormWindowManagerInterface.Action
        RaiseAction = ... # type: QDesignerFormWindowManagerInterface.Action
        UndoAction = ... # type: QDesignerFormWindowManagerInterface.Action
        RedoAction = ... # type: QDesignerFormWindowManagerInterface.Action
        HorizontalLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        VerticalLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        SplitHorizontalAction = ... # type: QDesignerFormWindowManagerInterface.Action
        SplitVerticalAction = ... # type: QDesignerFormWindowManagerInterface.Action
        GridLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        FormLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        BreakLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        AdjustSizeAction = ... # type: QDesignerFormWindowManagerInterface.Action
        SimplifyLayoutAction = ... # type: QDesignerFormWindowManagerInterface.Action
        DefaultPreviewAction = ... # type: QDesignerFormWindowManagerInterface.Action
        FormWindowSettingsDialogAction = ... # type: QDesignerFormWindowManagerInterface.Action

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def showPluginDialog(self) -> None: ...
    def closeAllPreviews(self) -> None: ...
    def showPreview(self) -> None: ...
    def actionGroup(self, actionGroup: 'QDesignerFormWindowManagerInterface.ActionGroup') -> typing.Optional[QtGui.QActionGroup]: ...
    def action(self, action: 'QDesignerFormWindowManagerInterface.Action') -> typing.Optional[QtGui.QAction]: ...
    def setActiveFormWindow(self, formWindow: typing.Optional[QDesignerFormWindowInterface]) -> None: ...
    def removeFormWindow(self, formWindow: typing.Optional[QDesignerFormWindowInterface]) -> None: ...
    def addFormWindow(self, formWindow: typing.Optional[QDesignerFormWindowInterface]) -> None: ...
    formWindowSettingsChanged: typing.ClassVar[QtCore.pyqtSignal]
    activeFormWindowChanged: typing.ClassVar[QtCore.pyqtSignal]
    formWindowRemoved: typing.ClassVar[QtCore.pyqtSignal]
    formWindowAdded: typing.ClassVar[QtCore.pyqtSignal]
    def core(self) -> typing.Optional[QDesignerFormEditorInterface]: ...
    def createFormWindow(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> typing.Optional[QDesignerFormWindowInterface]: ...
    def formWindow(self, index: int) -> typing.Optional[QDesignerFormWindowInterface]: ...
    def formWindowCount(self) -> int: ...
    def activeFormWindow(self) -> typing.Optional[QDesignerFormWindowInterface]: ...
    def actionSimplifyLayout(self) -> typing.Optional[QtGui.QAction]: ...
    def actionFormLayout(self) -> typing.Optional[QtGui.QAction]: ...


class QDesignerObjectInspectorInterface(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget], flags: QtCore.Qt.WindowType = ...) -> None: ...

    def setFormWindow(self, formWindow: typing.Optional[QDesignerFormWindowInterface]) -> None: ...
    def core(self) -> typing.Optional[QDesignerFormEditorInterface]: ...


class QDesignerPropertyEditorInterface(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget], flags: QtCore.Qt.WindowType = ...) -> None: ...

    def setReadOnly(self, readOnly: bool) -> None: ...
    def setPropertyValue(self, name: typing.Optional[str], value: typing.Any, changed: bool = ...) -> None: ...
    def setObject(self, object: typing.Optional[QtCore.QObject]) -> None: ...
    propertyChanged: typing.ClassVar[QtCore.pyqtSignal]
    def currentPropertyName(self) -> str: ...
    def object(self) -> typing.Optional[QtCore.QObject]: ...
    def isReadOnly(self) -> bool: ...
    def core(self) -> typing.Optional[QDesignerFormEditorInterface]: ...


class QDesignerWidgetBoxInterface(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...

    def save(self) -> bool: ...
    def load(self) -> bool: ...
    def fileName(self) -> str: ...
    def setFileName(self, file_name: typing.Optional[str]) -> None: ...


class QDesignerContainerExtension(PyQt6.sip.simplewrapper):

    def __init__(self) -> None: ...

    def canRemove(self, index: int) -> bool: ...
    def canAddWidget(self) -> bool: ...
    def remove(self, index: int) -> None: ...
    def insertWidget(self, index: int, widget: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def addWidget(self, widget: typing.Optional[QtWidgets.QWidget]) -> None: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def currentIndex(self) -> int: ...
    def widget(self, index: int) -> typing.Optional[QtWidgets.QWidget]: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QDesignerCustomWidgetInterface(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerCustomWidgetInterface') -> None: ...

    def codeTemplate(self) -> str: ...
    def domXml(self) -> str: ...
    def initialize(self, core: typing.Optional[QDesignerFormEditorInterface]) -> None: ...
    def isInitialized(self) -> bool: ...
    def createWidget(self, parent: typing.Optional[QtWidgets.QWidget]) -> typing.Optional[QtWidgets.QWidget]: ...
    def isContainer(self) -> bool: ...
    def icon(self) -> QtGui.QIcon: ...
    def includeFile(self) -> str: ...
    def whatsThis(self) -> str: ...
    def toolTip(self) -> str: ...
    def group(self) -> str: ...
    def name(self) -> str: ...


class QDesignerCustomWidgetCollectionInterface(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDesignerCustomWidgetCollectionInterface') -> None: ...

    def customWidgets(self) -> typing.List[QDesignerCustomWidgetInterface]: ...


class QAbstractExtensionFactory(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAbstractExtensionFactory') -> None: ...

    def extension(self, object: typing.Optional[QtCore.QObject], iid: typing.Optional[str]) -> typing.Optional[QtCore.QObject]: ...


class QExtensionFactory(QtCore.QObject, QAbstractExtensionFactory):

    def __init__(self, parent: typing.Optional['QExtensionManager'] = ...) -> None: ...

    def createExtension(self, object: typing.Optional[QtCore.QObject], iid: typing.Optional[str], parent: typing.Optional[QtCore.QObject]) -> typing.Optional[QtCore.QObject]: ...
    def extensionManager(self) -> typing.Optional['QExtensionManager']: ...
    def extension(self, object: typing.Optional[QtCore.QObject], iid: typing.Optional[str]) -> typing.Optional[QtCore.QObject]: ...


class QAbstractExtensionManager(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAbstractExtensionManager') -> None: ...

    def extension(self, object: typing.Optional[QtCore.QObject], iid: typing.Optional[str]) -> typing.Optional[QtCore.QObject]: ...
    def unregisterExtensions(self, factory: typing.Optional[QAbstractExtensionFactory], iid: typing.Optional[str]) -> None: ...
    def registerExtensions(self, factory: typing.Optional[QAbstractExtensionFactory], iid: typing.Optional[str]) -> None: ...


class QFormBuilder(QAbstractFormBuilder):

    def __init__(self) -> None: ...

    def customWidgets(self) -> typing.List[QDesignerCustomWidgetInterface]: ...
    def setPluginPath(self, pluginPaths: typing.Iterable[typing.Optional[str]]) -> None: ...
    def addPluginPath(self, pluginPath: typing.Optional[str]) -> None: ...
    def clearPluginPaths(self) -> None: ...
    def pluginPaths(self) -> typing.List[str]: ...


class QDesignerMemberSheetExtension(PyQt6.sip.simplewrapper):

    def __init__(self) -> None: ...

    def parameterNames(self, index: int) -> typing.List[QtCore.QByteArray]: ...
    def parameterTypes(self, index: int) -> typing.List[QtCore.QByteArray]: ...
    def signature(self, index: int) -> str: ...
    def declaredInClass(self, index: int) -> str: ...
    def inheritedFromWidget(self, index: int) -> bool: ...
    def isSlot(self, index: int) -> bool: ...
    def isSignal(self, index: int) -> bool: ...
    def setVisible(self, index: int, b: bool) -> None: ...
    def isVisible(self, index: int) -> bool: ...
    def setMemberGroup(self, index: int, group: typing.Optional[str]) -> None: ...
    def memberGroup(self, index: int) -> str: ...
    def memberName(self, index: int) -> str: ...
    def indexOf(self, name: typing.Optional[str]) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QDesignerPropertySheetExtension(PyQt6.sip.simplewrapper):

    def __init__(self) -> None: ...

    def isEnabled(self, index: int) -> bool: ...
    def setChanged(self, index: int, changed: bool) -> None: ...
    def isChanged(self, index: int) -> bool: ...
    def setProperty(self, index: int, value: typing.Any) -> None: ...
    def property(self, index: int) -> typing.Any: ...
    def setAttribute(self, index: int, b: bool) -> None: ...
    def isAttribute(self, index: int) -> bool: ...
    def setVisible(self, index: int, b: bool) -> None: ...
    def isVisible(self, index: int) -> bool: ...
    def reset(self, index: int) -> bool: ...
    def hasReset(self, index: int) -> bool: ...
    def setPropertyGroup(self, index: int, group: typing.Optional[str]) -> None: ...
    def propertyGroup(self, index: int) -> str: ...
    def propertyName(self, index: int) -> str: ...
    def indexOf(self, name: typing.Optional[str]) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...


class QExtensionManager(QtCore.QObject, QAbstractExtensionManager):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def extension(self, object: typing.Optional[QtCore.QObject], iid: typing.Optional[str]) -> typing.Optional[QtCore.QObject]: ...
    def unregisterExtensions(self, factory: typing.Optional[QAbstractExtensionFactory], iid: typing.Optional[str] = ...) -> None: ...
    def registerExtensions(self, factory: typing.Optional[QAbstractExtensionFactory], iid: typing.Optional[str] = ...) -> None: ...


class QDesignerTaskMenuExtension(PyQt6.sip.simplewrapper):

    def __init__(self) -> None: ...

    def preferredEditAction(self) -> typing.Optional[QtGui.QAction]: ...
    def taskActions(self) -> typing.List[QtGui.QAction]: ...


class QPyDesignerContainerExtension(QtCore.QObject, QDesignerContainerExtension):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...


class QPyDesignerCustomWidgetCollectionPlugin(QtCore.QObject, QDesignerCustomWidgetCollectionInterface):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...


class QPyDesignerCustomWidgetPlugin(QtCore.QObject, QDesignerCustomWidgetInterface):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...


class QPyDesignerTaskMenuExtension(QtCore.QObject, QDesignerTaskMenuExtension):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...


class QPyDesignerPropertySheetExtension(QtCore.QObject, QDesignerPropertySheetExtension):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...


class QPyDesignerMemberSheetExtension(QtCore.QObject, QDesignerMemberSheetExtension):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...
