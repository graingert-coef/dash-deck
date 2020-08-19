# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DeckGL(Component):
    """A DeckGL component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- json (dict; optional): The JSON representation of your map. This can be generated by calling
pdk.Deck(...).to_json()
- id (string; optional): The ID used to identify this component in Dash callbacks.
- mapboxApiAccessToken (string; optional): `mapboxApiAccessToken` (text) = You will need a mapbox token to use deck.gl. Please create a mapbox
and follow the instructions here: https://docs.mapbox.com/help/how-mapbox-works/access-tokens/
- clickEvent (dict; optional): This prop is updated when an element in the map is clicked. This contains
the original gesture event (in JSON).
- clickInfo (dict; optional): This prop is updated when an element in the map is clicked. This contains
the picking info describing the object being clicked.

Complete description here:
https://deck.gl/docs/developer-guide/interactivity#the-picking-info-object
- hoverEvent (dict; optional): This prop is updated when an element in the map is hovered. This contains
the original gesture event (in JSON).
- hoverInfo (dict; optional): This prop is updated when an element in the map is hovered. This contains
the picking info describing the object being hovered.

Complete description here:
https://deck.gl/docs/developer-guide/interactivity#the-picking-info-object
- dragStartEvent (dict; optional): This prop is updated when the user starts dragging on the canvas. This contains
the original gesture event (in JSON).
- dragStartInfo (dict; optional): This prop is updated when the user starts dragging on the canvas. This contains
the picking info describing the object being dragged.

Complete description here:
https://deck.gl/docs/developer-guide/interactivity#the-picking-info-object
- dragEndEvent (dict; optional): This prop is updated when the user releases from dragging the canvas. This contains
the original gesture event (in JSON).
- dragEndInfo (dict; optional): This prop is updated when the user releases from dragging the canvas. This contains
the picking info describing the object being dragged.

Complete description here:
https://deck.gl/docs/developer-guide/interactivity#the-picking-info-object"""
    @_explicitize_args
    def __init__(self, json=Component.UNDEFINED, id=Component.UNDEFINED, mapboxApiAccessToken=Component.UNDEFINED, clickEvent=Component.UNDEFINED, clickInfo=Component.UNDEFINED, hoverEvent=Component.UNDEFINED, hoverInfo=Component.UNDEFINED, dragStartEvent=Component.UNDEFINED, dragStartInfo=Component.UNDEFINED, dragEndEvent=Component.UNDEFINED, dragEndInfo=Component.UNDEFINED, **kwargs):
        self._prop_names = ['json', 'id', 'mapboxApiAccessToken', 'clickEvent', 'clickInfo', 'hoverEvent', 'hoverInfo', 'dragStartEvent', 'dragStartInfo', 'dragEndEvent', 'dragEndInfo']
        self._type = 'DeckGL'
        self._namespace = 'dash_deck'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['json', 'id', 'mapboxApiAccessToken', 'clickEvent', 'clickInfo', 'hoverEvent', 'hoverInfo', 'dragStartEvent', 'dragStartInfo', 'dragEndEvent', 'dragEndInfo']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DeckGL, self).__init__(**args)
