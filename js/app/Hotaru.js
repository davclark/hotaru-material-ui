/**
 * In this file, we create a React component
 * which incorporates components provided by Material-UI.
 */
import React, {Component} from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import IconButton from 'material-ui/IconButton';
import Dialog from 'material-ui/Dialog';
import {deepOrange500} from 'material-ui/styles/colors';
import Toggle from 'material-ui/Toggle';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Slider from 'material-ui/Slider';

const styles = {
  container: {
    textAlign: 'center',
    paddingTop: 200,
  },
  labelText: {
    paddingTop: 200,
  },
  Slider: {
    backgroundColor: "#ff0000",
  },
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
  constructor(props) {
    super(props);
    this.state = {active: false, r: 255, g: 255, b: 255};

    // Make this work in callbacks
    this.handleToggle = this.handleToggle.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);
    this.handleRedChange = this.handleRedChange.bind(this);

  }

  switch(onoff) {
    let url = `/api/lights/${onoff}?r=${this.state.r}`;

    // This is all not rather careful...
    return fetch(url)
        .then(response => response.json())
        .then(json => {this.setState({active: json.status.active})});
  }

  handleToggle(event) {
    // Interestingly, the following line always provides value="on" no matter
    // what!
    // console.log(event.target)

    if(this.state.active) {
        this.switch('off');
    }
    else {
        this.switch('on');
    }
  }

  handleUpdate(event) {
    // Note, this logic is somewhat the reverse of handleToggle
    // We are updating color, not flipping the switch
    if(this.state.active) {
        this.switch('on');
    }
  }

  handleRedChange(event, value) {
      this.state.r = value;
  }
  handleGreenChange(event, value) {
      this.state.g = value;
  }
  handleBlueChange(event, value) {
      this.state.b = value;
  }
  render() {
    return (
      <MuiThemeProvider muiTheme={muiTheme}>
        <div>
          <AppBar
              title="Hotaru"
              className="accent1Color"
          />
          <Toggle
              label="Power"
              toggled={this.state.active}
              onToggle={this.handleToggle}
          />
          <Slider
              value={this.state.r}
              onChange={this.handleRedChange}
              onDragStop={this.handleUpdate}
              max={255}
              step={1}
              style={{trackColor: "#ff0000"}}
          />
          <Slider
              value={this.state.g}
              onChange={this.handleGreenChange}
              onDragStop={this.handleUpdate}
              max={255}
              step={1}
              style={{trackColor: "#ff0000"}}
          />
          <Slider
              value={this.state.b}
              onChange={this.handleBlueChange}
              onDragStop={this.handleUpdate}
              max={255}
              step={1}
              style={{trackColor: "#ff0000"}}
          />
        </div>
      </MuiThemeProvider>
    );
  }
}

export default Hotaru;
