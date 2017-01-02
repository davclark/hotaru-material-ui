Hotaru_web
==========

A morepath web interface for blinky lights.

Morepath backend
----------------

You can run the code using a clean Python environment (using virtualenv)

  $ virtualenv env
  $ source env/bin/activate

After this you can install dependencies using

  $ env/bin/pip install -e .

Once that is done you can start the server

  $ env/bin/run-app

You can go to http://localhost:5000 to see the UI. To allow external requests,
use

  $ env/bin/run-app --host 0.0.0.0

For installing the test suite and running the tests use

  $ env/bin/pip install -e '.[test]'
  $ env/bin/py.test



React / Material-UI Webpack Component
-------------------------------------

JS assets are organized with [Webpack](http://webpack.github.io/docs/), and
we're using [Material-UI](http://callemall.github.io/material-ui/).

### Installation

JavaScript code is in `js` subdirectory. To rebuild the bundle you
need to install the JS dependencies (listed in package.json).
After cloning the repository, install dependencies:
```sh
cd <project folder>/material-ui/examples/webpack-example
npm install
```

to install them. Then run

  $ npm run build

To rebuild the bundle after changing it.

You can run a local server with JUST the JS component:
```sh
npm start
```
Server is located at http://localhost:3000

Note: To allow external viewing of the demo, change the following value in `webpack-dev-server.config.js`

```
host: 'localhost'  //Change to '0.0.0.0' for external facing server
```
