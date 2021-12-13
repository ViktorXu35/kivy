'''
Widgets
=======

Widgets are elements of a graphical user interface that form part of the
`User Experience <http://en.wikipedia.org/wiki/User_experience>`_.
The `kivy.uix` module contains classes for creating and managing Widgets.
Please refer to the :doc:`api-kivy.uix.widget` documentation for further
information.

Kivy widgets can be categorized as follows:

- **UX widgets**: Classical user interface widgets, ready to be assembled to
  create more complex widgets.

    :doc:`api-kivy.uix.label`, :doc:`api-kivy.uix.button`,
    :doc:`api-kivy.uix.checkbox`,
    :doc:`api-kivy.uix.image`, :doc:`api-kivy.uix.slider`,
    :doc:`api-kivy.uix.progressbar`, :doc:`api-kivy.uix.textinput`,
    :doc:`api-kivy.uix.togglebutton`, :doc:`api-kivy.uix.switch`,
    :doc:`api-kivy.uix.video`

- **Layouts**: A layout widget does no rendering but just acts as a trigger
  that arranges its children in a specific way. Read more on
  :doc:`Layouts here <api-kivy.uix.layout>`.

    :doc:`api-kivy.uix.anchorlayout`, :doc:`api-kivy.uix.boxlayout`,
    :doc:`api-kivy.uix.floatlayout`,
    :doc:`api-kivy.uix.gridlayout`, :doc:`api-kivy.uix.pagelayout`,
    :doc:`api-kivy.uix.relativelayout`, :doc:`api-kivy.uix.scatterlayout`,
    :doc:`api-kivy.uix.stacklayout`

- **Complex UX widgets**: Non-atomic widgets that are the result of
  combining multiple classic widgets.
  We call them complex because their assembly and usage are not as
  generic as the classical widgets.

    :doc:`api-kivy.uix.bubble`, :doc:`api-kivy.uix.dropdown`,
    :doc:`api-kivy.uix.filechooser`, :doc:`api-kivy.uix.popup`,
    :doc:`api-kivy.uix.spinner`,
    :doc:`api-kivy.uix.recycleview`,
    :doc:`api-kivy.uix.tabbedpanel`, :doc:`api-kivy.uix.videoplayer`,
    :doc:`api-kivy.uix.vkeyboard`,

- **Behaviors widgets**: These widgets do no rendering but act on the
  graphics instructions or interaction (touch) behavior of their children.

    :doc:`api-kivy.uix.scatter`, :doc:`api-kivy.uix.stencilview`

- **Screen manager**: Manages screens and transitions when switching
  from one to another.

    :doc:`api-kivy.uix.screenmanager`

----
'''
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.video import Video

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.bubble import Bubble
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooser
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.recycleview import RecycleView
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.vkeyboard import VKeyboard

from kivy.uix.scatter import Scatter
from kivy.uix.stencilview import StencilView

from kivy.uix.screenmanager import ScreenManager
