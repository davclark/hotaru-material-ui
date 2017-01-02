from .app import App
from . import model


@App.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@App.path(model=model.Greeting, path='/greeting/{person}')
def get_greeting(person):
    return model.Greeting(person)


@App.path(model=model.Lights, path='/lights/{action}')
def light_switch(action):
    if action == 'on':
        model.lights.on()
    elif action == 'off':
        model.lights.off()

    return model.lights
