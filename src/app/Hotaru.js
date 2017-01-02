/**
 * In this file, we create a React component
 * which incorporates components provided by Material-UI.
 */
import React, {Component} from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import FontIcon from 'material-ui/FontIcon';
import Dialog from 'material-ui/Dialog';
import {deepOrange500} from 'material-ui/styles/colors';
import Toggle from 'material-ui/Toggle';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const styles = {
  container: {
    textAlign: 'center',
    paddingTop: 200,
  },
  labelText: {
    paddingTop: 200,
  }
};

const iconStyles = {
};


// Not currently using this, see Main.js for usage
const muiTheme = getMuiTheme({
  palette: {
    accent1Color: deepOrange500,
  },
});

class Hotaru extends Component {
  render() {
    return (
      <MuiThemeProvider muiTheme={muiTheme}>
        <div>
          <Toggle
              label="Power"
              defaultToggled={false}
          />
        </div>
      </MuiThemeProvider>
    );
  }
}

export default Hotaru;
