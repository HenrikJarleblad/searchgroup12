import React, { Component } from 'react';

class Question extends Component {

  render() {
    return(
      <div>
        <form>
          <label>
            Question:
            <input type="text" name="question" />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default Question;
