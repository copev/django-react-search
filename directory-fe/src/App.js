import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import SearchBar from "./components/SearchBar";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Search />
      </Fragment>
    );
  }
}

export default App;
