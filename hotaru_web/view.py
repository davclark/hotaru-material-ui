from .app import App
from . import model


@App.json(model=model.Root)
def view_root(self, request):
    return {
        'greetings': [
            {
                'name': greeting.person,
                '@id': request.link(greeting)
            }
            for greeting in self.greetings
        ]
    }


@App.json(model=model.Greeting)
def view_greeting(self, request):
    return {
        'greeting': 'hello ' + self.person
    }

@App.json(model=model.Lights)
def view_light_status(self, request):
    return {
        'status': self.status()
    }
