import React from 'react';
import { comments } from 'commentData';
import Card from 'Card';

function App(props) {
  return(
  <div>
  {
    comments.map(comment =>
    <Card commentObject = {comment}/>
    )
  }
  </div>
);
}
export default App;