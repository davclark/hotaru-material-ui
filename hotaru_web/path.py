from .app import App
from . import model


@App.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@App.path(model=model.Greeting, path='/greeting/{person}')
def get_greeting(person):
    return model.Greeting(person)


@App.path(model=model.Lights, path='/lights/{action}')
def light_switch(action, r, g, b):
    if action == 'on':
        # We don't convert to ints here (rather pass unicode strings),
        # as we don't want to special case None
        model.lights.on(r, g, b)
    elif action == 'off':
        # Currently we don't supply colors to off
        model.lights.off()

    return model.lights
