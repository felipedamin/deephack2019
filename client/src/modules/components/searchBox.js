import * as React from 'react';
import Autosuggest from 'react-autosuggest';

import getFromBD from '../helpers/getFromBD'
import './searchBox.css'

// Teach Autosuggest how to calculate suggestions for any given input value.

// When suggestion is clicked, Autosuggest needs to populate the input
// based on the clicked suggestion. Teach Autosuggest how to calculate the
// input value for every given suggestion.
const getSuggestionValue = suggestion => suggestion;

// Use your imagination to render suggestions.
const renderSuggestion = suggestion => (
  <div>
    {suggestion}
  </div>
);

export default class SearchBox extends React.Component {
  constructor(props) {
    super(props);
    // Autosuggest is a controlled component.
    // This means that you need to provide an input value
    // and an onChange handler that updates this value (see below).
    // Suggestions also need to be provided to the Autosuggest,
    // and they are initially empty because the Autosuggest is closed.
    this.state = {
      value: '',
      suggestions: [],
    }
    this.searchList()
  }
  
  async searchList() {
    try {
      let listaMunicipios = await getFromBD.getMunicipios()
      this.listaMunicipios = listaMunicipios
    } catch (err) {
      console.log(err)
    }
  }
  getSuggestions = value => {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;

    return inputLength < 3 ? [] : this.listaMunicipios.filter(cidades => {
      const filtrada = cidades.toLowerCase().slice(0, inputLength) === inputValue
      if (filtrada) {return cidades}
    });
  };

  onChange = (event, { newValue, method }) => {
    this.props.onChange(newValue, method!=='type')
    if (method==='escape') {
      this.props.onChange('', false)
    }
    /*this.setState({
      value: newValue
    });*/
  };

  // Autosuggest will call this function every time you need to update suggestions.
  // You already implemented this logic above, so just use it.
  onSuggestionsFetchRequested = ({ value }) => {
    const newSuggestions = this.getSuggestions(value)
    this.setState({ suggestions: newSuggestions });
  };

  // Autosuggest will call this function every time you need to clear suggestions.
  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };
  /*
  update = (event) => {
    if (event.type === 'change') {
      this.setState({ value: event.target.value })
      this.props.onChange(event.target.value, false)
    }
    else {
      this.setState({ value: this.state.suggestions[0]})
      this.props.onChange(this.state.suggestions[0], true)
      // console.log(document.getElementById('react-autowhatever-1'))
    }
  }
  */
  render() {
    const suggestions = this.state.suggestions;

    // Finally, render it!
    return (
      <Autosuggest
        suggestions={suggestions}
        onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
        onSuggestionsClearRequested={this.onSuggestionsClearRequested}
        getSuggestionValue={getSuggestionValue}
        renderSuggestion={renderSuggestion}
        inputProps={{
          placeholder: 'Digite o nome da cidade',
          value: this.props.cidade,
          onChange: this.onChange,
          type: 'search'
        }
        }
      />
    );
  }
}