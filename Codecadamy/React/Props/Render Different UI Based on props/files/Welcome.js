import React from 'react';

function Welcome(props) {
   if (props.name == 'Wolfgang Amadeus Mozart') {
      return <h2>Hello, Mozart</h2>
    } else {
      return <h2>Welcome to my website!</h2>
    }
}
export default Welcome;