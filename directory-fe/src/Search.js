import React, { Component } from "react";
import "./Search.css";

class Search extends Component {
  state = {
    searchValue: "",
    organizations: []
  };

  handleOnChange = event => {
    this.setState({ searchValue: event.target.value });
  };

  handleSearch = () => {
    this.makeApiCall(this.state.searchValue);
  };

  makeApiCall = searchInput => {
    var searchUrl = `http://localhost:8000/orgsearch/?search=${searchInput}`;
    fetch(searchUrl)
      .then(response => {
        return response.json();
      })
      .then(jsonData => {
        this.setState({ organizations: jsonData });
      });
  };

  render() {
    return (
      <div id="main">
        <h1>Collaboratory Organization Directory</h1>
        <input
          name="text"
          type="text"
          placeholder="Search"
          onChange={event => this.handleOnChange(event)}
          value={this.state.searchValue}
        />
        <button onClick={this.handleSearch}>Search</button>
        {this.state.organizations ? (
          <div id="orgs-container">
            {this.state.organizations.map((organization, index) => (
              <div class="single-org" key={index}>
                <h2>{organization.name}</h2>
                <h3> {organization.county} </h3>
              </div>
            ))}
          </div>
        ) : (
          <p>Try searching for another organization.</p>
        )}
      </div>
    );
  }
}

export default Search;